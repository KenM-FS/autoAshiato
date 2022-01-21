import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json

def honto_email():
    json_open = open('secret.json', 'r')
    json_key = json.load(json_open)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = json_key['MAIL_ADDRESS']
    smtp_pass = json_key['SMTP_PASS']

    to_address = smtp_user
    from_address = smtp_user
    subject = "Unusual status on Ashiato, honto"
    body = "Unusual status has been confirmed on Ashiato point, honto."
    filename = "screenshot"

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_address
    msg["To"] = to_address
    msg.attach(MIMEText(body, "html"))

    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()
    s.login(smtp_user, smtp_pass)
    s.send_message(msg)
    s.quit()

if __name__ == '__main__':
    honto_email()

