# 🧠 Simple CRM System (with Email Automation & Dashboard)

A lightweight Customer Relationship Management (CRM) tool that allows users to:
- 📇 Manage contacts and business deals
- 📋 Track tasks with due dates
- 📤 Automatically send task reminders via email (Gmail)
- 📊 View everything from a clean Streamlit dashboard

---

## 🖥️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python (Pandas, PyMySQL, smtplib)
- **Database**: MySQL
- **Email**: Gmail (App Passwords)
- **Scheduling**: Local task scheduler (e.g., Windows Task Scheduler)

---

## ⚙️ How the Automation Works

1. Every night, a Python script checks the MySQL database for tasks due the next day.
2. It fetches contact info and task details.
3. The script logs into Gmail using an app password.
4. Automatically sends reminder emails to each contact with a task due tomorrow.

### 🔁 Example Email Sent:
> Subject: Reminder: Task due on 2025-06-27  
> "Hello victor , this is a reminder that your task is due tomorrow..."

---

## 📅 How It's Scheduled

The script is scheduled to run automatically every day using **Windows Task Scheduler**:

- Python script: `send_reminders.py`
- Trigger: Daily @ 9:00 AM
- Runs quietly in the background — no user input needed

---

## 🙋‍♂️ Author

**Victor Atubeh**  
_Data Analyst with Automation Skills in Python, SQL, and Reporting_

🔗 https://www.linkedin.com/in/victor-atubeh-ba9825297/

---

> 💡 _Note: Passwords and credentials are not included in the public repo. To run this, plug in your own MySQL password and Gmail App Password._

