import pymysql
import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database connection
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='your_password',  # Replace with your MySQL password
    database='simple_crm'
)

# Get tomorrow's tasks
tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
query = """
SELECT t.task_description, t.due_date, c.name, c.email
FROM tasks t
JOIN contacts c ON t.contact_id = c.contact_id
WHERE t.due_date = %s AND t.is_completed = FALSE
"""
reminders_df = pd.read_sql(query, conn, params=(tomorrow,))
conn.close()

# Email credentials (Use Gmail App Password)
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"

# Setup Gmail connection
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender_email, sender_password)

# Send emails
for _, row in reminders_df.iterrows():
    name = row["name"]
    recipient = row["email"]
    task = row["task_description"]
    due = row["due_date"]

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = f"Reminder: Task due on {due}"

    body = f"""
    Hello {name},

    This is a reminder that your task is due tomorrow ({due}):

     Task: {task}

    Please take any needed action.

    Best regards,  
    Your CRM Bot
    """
    msg.attach(MIMEText(body, "plain"))
    server.send_message(msg)

server.quit()
print(" Reminder email sent successfully!")
