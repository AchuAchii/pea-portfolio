# PEA Portfolio Workspace

[English](#english) | [ภาษาไทย](#ภาษาไทย)

## English

This repository is a portfolio of projects I worked on around PEA-related energy and data tasks. It brings together analysis notebooks, small applications, workflow diagrams, and demos that reflect the kind of work I did in forecasting, data validation, and operational reporting.

The main themes in this repo are:

- renewable generation analysis
- solar power forecasting
- EGAT billing and reconciliation checks
- load trend analysis across multiple years
- small Python and web-based internal tools

## What This Portfolio Shows

Across the projects in this repo, my work includes:

- cleaning and combining energy datasets from multiple files and periods
- analyzing generation and load behavior with Python and notebooks
- building forecasting prototypes for solar generation and monthly demand-related metrics
- comparing source files to detect mismatches and reconciliation issues
- turning technical work into simple visual outputs such as charts, HTML demos, and process diagrams

## Tech Stack

- Python
- pandas
- NumPy
- scikit-learn
- statsmodels
- Flask
- pvlib
- Plotly
- Chart.js
- HTML, CSS, JavaScript

## Featured Projects

### 1. Solar Forecast Web App

Path: [`projects/solar-forecast-webapp/`](projects/solar-forecast-webapp/)

This project is a small web application for estimating hourly solar generation from weather data. It combines weather API data with PV system modeling to give a simple forecast view that a non-technical user can interact with.

What I worked on:

- built a Flask backend that fetches hourly weather data from Open-Meteo
- used `pvlib` to simulate PV output from site configuration and irradiance inputs
- added configurable loss parameters such as soiling, shading, mismatch, wiring, and degradation
- returned both hourly time-series data and summary metrics such as peak, total energy, capacity factor, and loss percentage
- connected the backend to a browser-based UI that visualizes generation and irradiance

Key files:

- [`projects/solar-forecast-webapp/app.py`](projects/solar-forecast-webapp/app.py)
- [`projects/solar-forecast-webapp/templates/index.html`](projects/solar-forecast-webapp/templates/index.html)
- [`projects/solar-forecast-webapp/test.html`](projects/solar-forecast-webapp/test.html)

Skills demonstrated:

- API integration
- energy forecasting logic
- backend and frontend integration
- data visualization

### 2. Renewable Generation Analysis

Path: [`projects/renewable-generation-analysis/`](projects/renewable-generation-analysis/)

This folder contains exploratory analysis and forecasting work for renewable generation data, especially solar, biomass, and biological fuel groups. The work focuses on understanding plant behavior, grouping similar assets, and testing solar forecast approaches.

What I worked on:

- prepared and filtered generation data by fuel type
- calculated summary indicators such as average efficiency, variability, and missing-rate behavior
- used K-Means clustering to group plants with similar performance patterns
- explored solar forecast approaches in notebooks using weather data and PV modeling
- generated visual outputs to inspect solar profiles and compare forecast behavior

Representative files:

- [`projects/renewable-generation-analysis/dataanalystphase1.ipynb`](projects/renewable-generation-analysis/dataanalystphase1.ipynb)
- [`projects/renewable-generation-analysis/dataanalysephase2.ipynb`](projects/renewable-generation-analysis/dataanalysephase2.ipynb)
- [`projects/renewable-generation-analysis/KmeansVspp.ipynb`](projects/renewable-generation-analysis/KmeansVspp.ipynb)
- [`projects/renewable-generation-analysis/groupkmean.ipynb`](projects/renewable-generation-analysis/groupkmean.ipynb)
- [`projects/renewable-generation-analysis/predictsolartest.ipynb`](projects/renewable-generation-analysis/predictsolartest.ipynb)
- [`projects/renewable-generation-analysis/finalforecast.ipynb`](projects/renewable-generation-analysis/finalforecast.ipynb)

Skills demonstrated:

- exploratory data analysis
- clustering and segmentation
- renewable energy performance analysis
- forecasting prototyping

### 3. EGAT Billing Audit

Path: [`projects/egat-billing-audit/`](projects/egat-billing-audit/)

This work focuses on checking and reconciling billing-related files between EGAT and internal processing outputs. The goal is to make mismatches visible and produce files that are easier to verify.

What I worked on:

- transformed consumption values into the required format for downstream checking
- compared source and processed files
- separated records that exist only in one source versus the other
- produced mismatch summaries to support manual review

Representative file:

- [`projects/egat-billing-audit/egat.ipynb`](projects/egat-billing-audit/egat.ipynb)

Skills demonstrated:

- reconciliation logic
- file comparison
- data validation
- operational reporting support

### 4. Load Trend Analysis

Path: [`projects/load-trend-analysis/`](projects/load-trend-analysis/)

This project analyzes load-related data across multiple years in order to identify trend changes, prepare merged yearly views, and derive comparable indicators for further monitoring.

What I worked on:

- read yearly files and normalized them into a comparable structure
- created derived monthly and average indicators from contract-related fields
- merged multiple years into one working dataset
- calculated year-over-year trend percentages
- added regional flags to support grouped analysis

Representative files:

- [`projects/load-trend-analysis/phase1.ipynb`](projects/load-trend-analysis/phase1.ipynb)
- [`projects/load-trend-analysis/phase2.ipynb`](projects/load-trend-analysis/phase2.ipynb)
- [`projects/load-trend-analysis/phase3.ipynb`](projects/load-trend-analysis/phase3.ipynb)

Skills demonstrated:

- multi-file data preparation
- feature engineering
- trend analysis
- notebook-based reporting

### 5. SARIMA Forecast Prototype

Path: [`projects/sarima-forecast-prototype/`](projects/sarima-forecast-prototype/)

This notebook is a time-series forecasting prototype for monthly unit-user data. It prepares the data, converts calendar fields into a proper time index, and uses a SARIMA-family model to forecast future values.

What I worked on:

- cleaned monthly data into a proper time-series format
- converted Buddhist Era years into Gregorian dates for modeling
- built a SARIMAX-based forecasting pipeline
- prepared the dataset for monthly forecasting and evaluation

Representative file:

- [`projects/sarima-forecast-prototype/projectforecast.ipynb`](projects/sarima-forecast-prototype/projectforecast.ipynb)

Skills demonstrated:

- time-series preprocessing
- statistical forecasting
- model prototyping

## Supporting Demos And Utilities

These files are smaller than the main projects, but they help show how I communicate ideas and build lightweight tools:

- [`demos/real-time-energy-chart.html`](demos/real-time-energy-chart.html)
  A simple front-end demo with simulated real-time bar and pie charts for energy usage and generation mix.
- [`demos/pea-process-diagram.html`](demos/pea-process-diagram.html)
  A workflow diagram showing billing and verification flow between EGAT, PEA units, and related teams.
- [`scripts/voltage-monitor-simulator.py`](scripts/voltage-monitor-simulator.py)
  A small Python script that simulates voltage dips and basic alert behavior.
- [`projects/python-pea-experiments/test.py`](projects/python-pea-experiments/test.py)
  A utility script for selecting and previewing CSV files through a simple desktop file picker.

## How To Review This Repo

If you are visiting this repository for the first time, the best order is:

1. Start with [`projects/solar-forecast-webapp/`](projects/solar-forecast-webapp/) to see an end-to-end application.
2. Continue with [`projects/renewable-generation-analysis/`](projects/renewable-generation-analysis/) for analysis, clustering, and forecasting experiments.
3. Open [`projects/egat-billing-audit/`](projects/egat-billing-audit/) to see reconciliation and validation work.
4. Review [`projects/load-trend-analysis/`](projects/load-trend-analysis/) and [`projects/sarima-forecast-prototype/`](projects/sarima-forecast-prototype/) for notebook-based analytical workflows.

## Important Note About This GitHub Version

This GitHub version is intentionally cleaned for portfolio use.

- raw data files are not included
- CSV and XLSX exports are not included
- ZIP archives are not included
- heavy generated HTML outputs that may embed data are not included
- notebook outputs were cleared before publishing

Because of that, some notebooks reference local source files that are not present in this public version. The focus of this repository is to show my workflow, logic, and project structure without exposing internal or raw data.

---

## ภาษาไทย

Repository นี้เป็น portfolio สำหรับรวบรวมงานที่ผมเคยทำเกี่ยวกับพลังงาน ข้อมูล และงานวิเคราะห์ในบริบทของ PEA โดยรวมทั้ง notebooks, web app ขนาดเล็ก, แผนภาพ workflow และ demo ต่าง ๆ ที่สะท้อนลักษณะงานที่ผมทำจริง เช่น forecasting, data validation และงานสนับสนุนเชิงปฏิบัติการ

หัวข้อหลักของงานใน repo นี้คือ:

- การวิเคราะห์ข้อมูลพลังงานทดแทน
- การพยากรณ์กำลังผลิตไฟฟ้าจากแสงอาทิตย์
- การตรวจสอบและกระทบยอดข้อมูล EGAT
- การวิเคราะห์แนวโน้มโหลดจากข้อมูลหลายปี
- เครื่องมือขนาดเล็กด้วย Python และ web

## Portfolio นี้แสดงอะไรบ้าง

จากงานที่รวมอยู่ใน repo นี้ สิ่งที่ผมทำมีทั้ง:

- ทำความสะอาดและรวมข้อมูลจากหลายไฟล์ หลายช่วงเวลา
- วิเคราะห์พฤติกรรมการผลิตและการใช้ไฟด้วย Python และ notebooks
- สร้างต้นแบบระบบ forecast สำหรับ solar generation และข้อมูลเชิงเวลา
- เปรียบเทียบไฟล์จากหลายแหล่งเพื่อหาความคลาดเคลื่อนและจุดที่ข้อมูลไม่ตรงกัน
- แปลงงานเชิงเทคนิคให้อยู่ในรูปที่สื่อสารง่ายขึ้น เช่น chart, HTML demo และ process diagram

## เครื่องมือที่ใช้

- Python
- pandas
- NumPy
- scikit-learn
- statsmodels
- Flask
- pvlib
- Plotly
- Chart.js
- HTML, CSS, JavaScript

## โปรเจกต์เด่น

### 1. Solar Forecast Web App

ที่อยู่: [`projects/solar-forecast-webapp/`](projects/solar-forecast-webapp/)

โปรเจกต์นี้เป็น web application ขนาดเล็กสำหรับประมาณการกำลังผลิตไฟฟ้าจากแสงอาทิตย์รายชั่วโมง โดยใช้ข้อมูลสภาพอากาศร่วมกับการจำลองระบบโซลาร์ เพื่อให้ผู้ใช้ทั่วไปสามารถกรอกพารามิเตอร์ของไซต์และดูผล forecast ได้ผ่านหน้าเว็บ

สิ่งที่ผมทำ:

- สร้าง Flask backend สำหรับดึงข้อมูลอากาศรายชั่วโมงจาก Open-Meteo
- ใช้ `pvlib` ในการจำลองกำลังผลิตของระบบ PV จากค่าพิกัด มุมติดตั้ง และข้อมูลรังสี
- เพิ่มตัวแปร loss ที่ปรับได้ เช่น soiling, shading, mismatch, wiring และ degradation
- ส่งออกทั้งข้อมูลรายชั่วโมงและค่า summary เช่น peak, total energy, capacity factor และ loss percentage
- เชื่อม backend เข้ากับหน้าเว็บที่แสดงกราฟกำลังผลิตและ irradiance

ไฟล์สำคัญ:

- [`projects/solar-forecast-webapp/app.py`](projects/solar-forecast-webapp/app.py)
- [`projects/solar-forecast-webapp/templates/index.html`](projects/solar-forecast-webapp/templates/index.html)
- [`projects/solar-forecast-webapp/test.html`](projects/solar-forecast-webapp/test.html)

ทักษะที่สะท้อน:

- การเชื่อมต่อ API
- logic ด้าน energy forecasting
- การเชื่อม backend และ frontend
- การทำ data visualization

### 2. Renewable Generation Analysis

ที่อยู่: [`projects/renewable-generation-analysis/`](projects/renewable-generation-analysis/)

โฟลเดอร์นี้เป็นงานวิเคราะห์และทดลอง forecast สำหรับข้อมูลพลังงานทดแทน โดยเน้นกลุ่ม solar, biomass และ biological เป็นหลัก จุดประสงค์คือเพื่อทำความเข้าใจพฤติกรรมของโรงไฟฟ้า จัดกลุ่มสินทรัพย์ที่มีรูปแบบคล้ายกัน และทดลองแนวทาง forecast สำหรับ solar generation

สิ่งที่ผมทำ:

- เตรียมและคัดกรองข้อมูลตามประเภทเชื้อเพลิง
- คำนวณตัวชี้วัดสำคัญ เช่น average efficiency, ความผันผวน และ missing-rate behavior
- ใช้ K-Means clustering เพื่อจัดกลุ่มโรงไฟฟ้าที่มีลักษณะการทำงานใกล้กัน
- ทดลองแนวทาง forecast สำหรับ solar ด้วย weather data และ PV modeling
- สร้าง output เชิงภาพเพื่อช่วยดูรูปแบบของ solar profile และเปรียบเทียบผล forecast

ไฟล์ตัวแทน:

- [`projects/renewable-generation-analysis/dataanalystphase1.ipynb`](projects/renewable-generation-analysis/dataanalystphase1.ipynb)
- [`projects/renewable-generation-analysis/dataanalysephase2.ipynb`](projects/renewable-generation-analysis/dataanalysephase2.ipynb)
- [`projects/renewable-generation-analysis/KmeansVspp.ipynb`](projects/renewable-generation-analysis/KmeansVspp.ipynb)
- [`projects/renewable-generation-analysis/groupkmean.ipynb`](projects/renewable-generation-analysis/groupkmean.ipynb)
- [`projects/renewable-generation-analysis/predictsolartest.ipynb`](projects/renewable-generation-analysis/predictsolartest.ipynb)
- [`projects/renewable-generation-analysis/finalforecast.ipynb`](projects/renewable-generation-analysis/finalforecast.ipynb)

ทักษะที่สะท้อน:

- exploratory data analysis
- clustering และ segmentation
- การวิเคราะห์ performance ของพลังงานทดแทน
- การทำ forecasting prototype

### 3. EGAT Billing Audit

ที่อยู่: [`projects/egat-billing-audit/`](projects/egat-billing-audit/)

งานชุดนี้เน้นการตรวจสอบและกระทบยอดไฟล์ที่เกี่ยวข้องกับ billing ระหว่าง EGAT และผลการประมวลผลภายใน เป้าหมายคือทำให้เห็น mismatch ได้ชัดขึ้น และเตรียมไฟล์ที่ตรวจสอบต่อได้ง่าย

สิ่งที่ผมทำ:

- แปลงค่าการใช้ไฟให้อยู่ในรูปแบบที่พร้อมสำหรับการตรวจสอบต่อ
- เปรียบเทียบข้อมูลระหว่างไฟล์ต้นทางและไฟล์หลังประมวลผล
- แยกรายการที่มีอยู่เฉพาะฝั่งใดฝั่งหนึ่ง
- สรุป mismatch เพื่อช่วยให้ตรวจทานด้วยมือได้ง่ายขึ้น

ไฟล์ตัวแทน:

- [`projects/egat-billing-audit/egat.ipynb`](projects/egat-billing-audit/egat.ipynb)

ทักษะที่สะท้อน:

- reconciliation logic
- การเปรียบเทียบไฟล์
- data validation
- งานสนับสนุนเชิงปฏิบัติการ

### 4. Load Trend Analysis

ที่อยู่: [`projects/load-trend-analysis/`](projects/load-trend-analysis/)

โปรเจกต์นี้เป็นการวิเคราะห์ข้อมูลโหลดจากหลายปี เพื่อหาการเปลี่ยนแปลงของแนวโน้ม จัดเตรียมมุมมองข้อมูลแบบรวมหลายปี และสร้างตัวชี้วัดที่ใช้เปรียบเทียบต่อได้

สิ่งที่ผมทำ:

- อ่านข้อมูลรายปีและปรับโครงสร้างให้อยู่ในรูปแบบที่เปรียบเทียบกันได้
- สร้างตัวแปรสรุปรายเดือนและค่าเฉลี่ยจากข้อมูลสัญญา
- รวมหลายปีเข้ามาเป็นชุดข้อมูลเดียวสำหรับการวิเคราะห์
- คำนวณเปอร์เซ็นต์แนวโน้มปีต่อปี
- เพิ่ม flag ตามภูมิภาคเพื่อใช้วิเคราะห์แบบ grouped analysis

ไฟล์ตัวแทน:

- [`projects/load-trend-analysis/phase1.ipynb`](projects/load-trend-analysis/phase1.ipynb)
- [`projects/load-trend-analysis/phase2.ipynb`](projects/load-trend-analysis/phase2.ipynb)
- [`projects/load-trend-analysis/phase3.ipynb`](projects/load-trend-analysis/phase3.ipynb)

ทักษะที่สะท้อน:

- การเตรียมข้อมูลจากหลายไฟล์
- feature engineering
