from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import requests
from datetime import datetime
from pvlib.location import Location
from pvlib.pvsystem import PVSystem
from pvlib.modelchain import ModelChain
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
from pvlib.irradiance import erbs

app = Flask(__name__)

# ────────── HELPERS ──────────

def get_weather(lat, lon, day: str) -> pd.DataFrame:
    """Fetch hourly weather (T, cloud, DNI, DHI) from Open-Meteo."""
    today  = datetime.now().date()
    target = datetime.strptime(day, "%Y-%m-%d").date()
    base   = ("https://archive-api.open-meteo.com/v1/archive"
              if target < today else
              "https://api.open-meteo.com/v1/forecast")
    params = ["temperature_2m","cloud_cover",
              "direct_normal_irradiance","diffuse_radiation"]
    url = (
        f"{base}?latitude={lat}&longitude={lon}"
        f"&hourly={','.join(params)}"
        f"&start_date={day}&end_date={day}"
        f"&timezone=Asia%2FBangkok"
    )
    data = requests.get(url, timeout=20).json()["hourly"]
    times = pd.to_datetime(data["time"]).tz_localize("Asia/Bangkok")

    wx = pd.DataFrame({
        'temp_air':    data["temperature_2m"],
        'cloud_cover': data.get("cloud_cover", [0]*len(times)),
        'dni':         data["direct_normal_irradiance"],
        'dhi':         data.get("diffuse_radiation", [0]*len(times)),
    }, index=times)

    # compute GHI
    solpos   = Location(lat, lon).get_solarposition(times)
    zenith   = solpos['zenith']
    wx['ghi'] = (wx['dni'] * np.cos(np.radians(zenith)) + wx['dhi']).clip(lower=0)

    # if DHI==0 (archive) decompose
    if wx['dhi'].sum() == 0:
        decomp    = erbs(wx['ghi'], zenith, times)
        wx['dhi'] = decomp['dhi']
        wx['dni'] = decomp['dni']

    return wx

def calculate_dynamic_loss(wx: pd.DataFrame, losses: dict) -> float:
    """Adjust shading loss by average cloud cover, then total."""
    avg_cloud = wx['cloud_cover'].mean() / 100
    losses     = losses.copy()
    losses['shading'] *= (1 + avg_cloud)
    eff        = np.prod([(1 - v/100) for v in losses.values()])
    return (1 - eff) * 100

def simulate_pv(wx: pd.DataFrame,
                kw_dc: float,
                tilt: float,
                azimuth: float,
                losses: dict) -> (pd.DataFrame, dict):
    """Run PV simulation (pvwatts) and return time series + summary."""
    eff = 0.9
    system = PVSystem(
        surface_tilt=tilt,
        surface_azimuth=azimuth,
        module_parameters={'pdc0': kw_dc * eff, 'gamma_pdc': -0.004},
        inverter_parameters={'pdc0': kw_dc * eff * 1.05, 'eta_inv_nom': 0.97},
        temperature_model_parameters=TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
    )
    loc = Location(wx.index.tz_localize(None)[0].tzinfo.zone, wx.index[0].tzinfo)
    mc  = ModelChain(system, loc, dc_model='pvwatts', ac_model='pvwatts', aoi_model='no_loss')
    mc.run_model(wx)

    loss_pct = calculate_dynamic_loss(wx, losses)
    ac_net   = (mc.results.ac * (1 - loss_pct/100)).clip(lower=0)

    df = pd.DataFrame({
        'time':       wx.index.strftime("%H:%M"),
        'pacRaw':     mc.results.ac.values.tolist(),
        'pacNet':     ac_net.values.tolist(),
        'ghi':        wx['ghi'].values.tolist(),
        'dni':        wx['dni'].values.tolist(),
    })
    summary = {
        'peak':       float(df['pacNet'].max()),
        'totalKwh':   float(df['pacNet'].sum() / 1000),
        'cf':         None,  # will compute below
        'lossPct':    float(loss_pct)
    }
    summary['cf'] = summary['totalKwh'] / (kw_dc * 24 / 1000) * 100
    return df, summary

# ────────── FLASK ROUTES ──────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/forecast')
def api_forecast():
    # read query params
    date    = request.args.get('date')
    lat     = float(request.args.get('lat'))
    lon     = float(request.args.get('lon'))
    alt     = float(request.args.get('alt', 50))
    kw_dc   = float(request.args.get('kw', 5000))
    tilt    = float(request.args.get('tilt', 15))
    azimuth = float(request.args.get('az', 180))
    # losses come in as multiple params
    keys = ['soiling','shading','mismatch','wiring','connections',
            'lid','nameplate','availability','degradation']
    losses = {k: float(request.args.get(k, 0)) for k in keys}

    # fetch weather & simulate
    wx  = get_weather(lat, lon, date)
    df, summary = simulate_pv(wx, kw_dc, tilt, azimuth, losses)

    return jsonify({
        'data':    df.to_dict(orient='records'),
        'summary': summary
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')