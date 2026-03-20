import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

def upload_csv():
    root = tk.Tk()
    root.withdraw()  # ไม่แสดงหน้าต่างหลัก

    file_path = filedialog.askopenfilename(
        title="เลือกไฟล์ CSV ที่ต้องการอัปโหลด",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    if file_path:
        print(f"\n📁 ไฟล์ที่เลือก: {os.path.basename(file_path)}\n")
        try:
            df = pd.read_csv(file_path)
            print("📄 ตัวอย่างข้อมูลจากไฟล์:\n")
            print(df.head())
        except Exception as e:
            print(f"❌ อ่านไฟล์ไม่สำเร็จ: {e}")
    else:
        print("⚠️ ไม่มีการเลือกไฟล์")

if __name__ == "__main__":
    upload_csv()
