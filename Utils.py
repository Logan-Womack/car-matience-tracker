import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import sys
load_dotenv('.env')

def send_email(subject, body, sender_email, receiver_email, password):
    """
    Send an email using SMTP with the provided subject, body, sender, receiver, and password.
    Args:
        subject (str): Subject of the email.
        body (str): Body content of the email.
        sender_email (str): Email address of the sender.
        receiver_email (str): Email address of the receiver.
        password (str): Google App Password for the sender's email account.
    Returns:
        None
    """
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email #", ".join(receiver_email)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender_email, password)
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully!')


def check_maintenance_due(mileage, log_dict, frequency_dict):
    """
    Check if any maintenance tasks are due based on the current mileage and the maintenance log.
    
    Args:
        mileage (int): Current mileage of the vehicle.
        log_dict (dict): Dictionary containing maintenance tasks and their last performed mileage.
        frequency_dict (dict): Dictionary containing maintenance tasks and their frequency in miles.
    
    Returns:
        list: List of maintenance tasks that are due.
    """
    due_tasks = []
    for task, last_mileage in log_dict.items():
        if mileage - last_mileage >= frequency_dict[task]:
            due_tasks.append(task)
    return due_tasks



# Example usage
if __name__ == "__main__":
    subject = 'Daily Report'
    body = 'This is a test email sent from Python using smtplib. in the car maintenance tracker project.'
    sender_email = os.getenv('email')
    receiver_email = os.getenv('email')
    password = os.getenv('python_email_connector_token')
    send_email(subject, body, sender_email, receiver_email, password)
    