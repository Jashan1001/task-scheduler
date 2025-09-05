import smtplib
from email.mime.text import MIMEText

def send_email(user_email, user_password, recipient, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = user_email
    msg['To'] = recipient

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(user_email, user_password)
        server.sendmail(user_email, recipient, msg.as_string())
