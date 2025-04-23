# monitor.py
import psutil

def get_system_stats():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "processes": len(psutil.pids())
    }
import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(cpu_usage):
    sender_email = "email@example.com"
    receiver_email = "receiver@example.com"
    password = "@Danger!"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"Alert: High CPU Usage ({cpu_usage}%)"
    
    body = f"Warning! CPU usage has exceeded 80%. Current usage: {cpu_usage}%"
    msg.attach(MIMEText(body, 'plain'))
    
    # Sending email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    processes = len(psutil.pids())

    # Send email if CPU usage > 80%
    if cpu_usage > 80:
        send_email_alert(cpu_usage)
    
    return {
        "cpu": cpu_usage,
        "memory": memory_usage,
        "disk": disk_usage,
        "processes": processes
    }
#This will send an email alert when CPU usage exceeds 80%. You’ll need to replace the sender_email, receiver_email, and password with actual values.