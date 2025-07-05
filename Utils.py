import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import sys
load_dotenv('.env')

def send_email(subject, body, sender_email, receiver_email, password):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email #", ".join(receiver_email)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender_email, password)
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully!')

if __name__ == "__main__":
    subject = 'Daily Report'
    body = 'This is a test email sent from Python using smtplib. in the car maintenance tracker project.'
    sender_email = os.getenv('email')
    receiver_email = os.getenv('email')
    password = os.getenv('python_email_connector_token')
    send_email(subject, body, sender_email, receiver_email, password)
    