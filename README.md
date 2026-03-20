# PEA Portfolio Workspace

โฟลเดอร์นี้ถูกจัดใหม่เพื่อให้ดูง่ายขึ้นและหยิบไปทำ portfolio ได้สะดวก โดยแยกงานออกเป็นหมวดหลักแทนการวางไฟล์ปะปนกันไว้ที่ root

เวอร์ชันที่เตรียมขึ้น GitHub จะเก็บเฉพาะงานที่ใช้โชว์ได้ เช่น source code, notebooks, demos, templates และเอกสารประกอบ โดยไม่รวม raw data, CSV/XLSX exports และไฟล์ zip สำรอง

## โครงสร้างหลัก

- `projects/` โปรเจกต์หลัก แยกตามงาน
- `data/` ข้อมูลดิบและไฟล์ export
- `docs/` เอกสารและสไลด์ประกอบ
- `demos/` ไฟล์ HTML เดโมหรือแผนภาพที่เปิดดูได้ทันที
- `scripts/` สคริปต์ Python แบบ standalone
- `archives/` ไฟล์ zip สำรอง

## Project Map

- `projects/solar-forecast-webapp/`
  Flask web app สำหรับ forecast พลังงานแสงอาทิตย์จาก weather API และ `pvlib`
- `projects/renewable-generation-analysis/`
  งานวิเคราะห์ข้อมูลพลังงานทดแทน เช่น solar, biomass, biological, clustering และ forecast outputs
- `projects/egat-billing-audit/`
  งานตรวจสอบและเทียบข้อมูล EGAT / billing / mismatch
- `projects/load-trend-analysis/`
  phase notebooks และข้อมูลรายปีสำหรับวิเคราะห์แนวโน้ม
- `projects/sarima-forecast-prototype/`
  notebook ทดลอง forecast ล่วงหน้า 12 เดือนพร้อมผลลัพธ์
- `projects/python-pea-experiments/`
  สคริปต์ Python ขนาดเล็กและไฟล์ทดลองประกอบ

## Recommended For Portfolio

ถ้าจะเริ่มทำพอร์ตจากของที่มีอยู่ตอนนี้ แนะนำหยิบ 3 กลุ่มนี้ไป polish ก่อน

1. `projects/solar-forecast-webapp/`
   เหมาะกับการโชว์งาน end-to-end ทั้ง data, model, API และ UI
2. `projects/renewable-generation-analysis/`
   เหมาะกับการโชว์ data analysis, clustering, visualization และ forecast
3. `projects/egat-billing-audit/`
   เหมาะกับการโชว์โจทย์ธุรกิจจริงด้าน data validation และ reconciliation

## สิ่งที่ควรทำต่อ

- เพิ่ม `README.md` ในแต่ละโปรเจกต์ให้มี `objective / data / tools / result`
- เลือก screenshot หรือ output HTML จากแต่ละโปรเจกต์ไปทำหน้า portfolio
- คัดไฟล์ output ที่ซ้ำหรือเก่าออกอีกครั้งเมื่อเริ่มคัดงานที่จะยื่นจริง
