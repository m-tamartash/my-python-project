# استفاده از image پایه پایتون ۳.۱۲.۳
FROM python:3.12.3-slim

# تنظیم دایرکتوری کاری داخل کانتینر
WORKDIR /app

# کپی فایل requirements.txt به داخل کانتینر
COPY requirements.txt .

# نصب dependencies پروژه
RUN pip install --no-cache-dir -r requirements.txt

# کپی تمام فایل‌های پروژه به داخل کانتینر
COPY . .

# دستور اجرای برنامه (اگر اسکریپت اصلی شما main.py است)
CMD ["python", "main.py"]