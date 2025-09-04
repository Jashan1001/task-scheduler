import os
import smtplib, ssl
from email.mime.text import MIMEText

# Lambda will read these from environment variables (set in AWS console)
SENDER = os.environ.get("SENDER_EMAIL")
RECEIVER = os.environ.get("RECEIVER_EMAIL")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

def send_email():
    if not SENDER or not RECEIVER or not SMTP_PASSWORD:
        print("❌ Missing email credentials in Lambda environment variables.")
        return {"ok": False, "error": "missing env vars"}

    msg = MIMEText("🔔 Reminder: AWS Lambda just ran your task!")
    msg["Subject"] = "Task Scheduler Reminder (Lambda)"
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER, SMTP_PASSWORD)
            server.sendmail(SENDER, [RECEIVER], msg.as_string())
        print("✅ Email sent from Lambda")
        return {"ok": True}
    except Exception as e:
        print(f"❌ Error in Lambda: {e}")
        return {"ok": False, "error": str(e)}

def lambda_handler(event, context):
    return send_email()
