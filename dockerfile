# استخدم صورة Python كأساس
FROM python:3.9-slim

# تعيين دليل العمل داخل الحاوية
WORKDIR /app

# نسخ ملف requirements.txt وتثبيت التبعيات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع إلى دليل العمل في الحاوية
COPY . .

# تحديد الأمر لتشغيل البوت
CMD ["python", "code.py"]
