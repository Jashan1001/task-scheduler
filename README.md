# Automated Task Scheduler with Cloud Deployment

This project is a Python-based task scheduler that can send automated reminders via email.  
It has two parts:
1. **Local Scheduler** – Runs on your laptop using the `schedule` library.
2. **Cloud Deployment** – Runs on **AWS Lambda** with **EventBridge** for automated cloud-based scheduling.

---

## 🚀 Features
- Local scheduling with Python
- Email notifications (via Gmail SMTP)
- Cloud deployment on AWS Lambda
- EventBridge scheduling (serverless automation)
- CI/CD with GitHub Actions (in progress)

---

## 🛠️ Tech Stack
- Python 3.13
- `schedule` library
- Gmail SMTP (App Password)
- AWS Lambda & EventBridge
- GitHub Actions

---

## 📂 Project Structure
task_scheduler/
├── local_schedule.py # Local Python scheduler
├── lambda_function.py # AWS Lambda function
├── .gitignore # Ignore env + cache
├── README.md # Project documentation
└── .env (not uploaded) # Secrets file (Gmail + password)


---

## ✨ How It Works
- The **local version** runs a Python script that sends email reminders every few minutes.  
- The **cloud version** runs the same logic in **AWS Lambda**, triggered by **EventBridge**.  

----