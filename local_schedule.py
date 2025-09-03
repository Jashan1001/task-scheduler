import os, time, schedule, smtplib, ssl, datetime
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SENDER = os.getenv("SENDER_EMAIL")
RECEIVER = os.getenv("RECEIVER_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

def send_email():
    msg = MIMEText(f"🔔 Reminder: Task ran at {datetime.datetime.now()}")
    msg["Subject"] = "Task Scheduler Reminder"
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER, SMTP_PASSWORD)
        server.sendmail(SENDER, [RECEIVER], msg.as_string())

    print("✅ Email sent!")

# Schedule email every 1 minute
schedule.every(1).minutes.do(send_email)

print("📧 Scheduler with email started… Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
