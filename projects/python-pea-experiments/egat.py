import random
import time

def read_voltage():
    # จำลองค่าไฟ (random วูบบางช่วง)
    if random.random() < 0.05:
        return random.uniform(180, 190)  # วูบ
    return random.uniform(220, 240)      # ปกติ

def check_voltage(voltage, threshold=200):
    return voltage < threshold

def monitor(threshold=200):
    print("เริ่มตรวจสอบสัญญาณไฟ...\n")
    while True:
        voltage = read_voltage()  # ค่าแรงดันที่อ่านได้
        print(f"Voltage: {voltage:.2f} V")
        
        if check_voltage(voltage, threshold):
            print("⚠️ แจ้งเตือน: ไฟวูบต่ำกว่าเกณฑ์ ! ⚠️")

        time.sleep(1)  # อ่านค่าทุก 1 วินาที

monitor()