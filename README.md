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

## 📸 Screenshots

### 🔹 Streamlit CRM Dashboard  
![Dashboard](dashboard_view.png)

### 🔹 Upcoming Tasks with Reminder Section  
![Reminders](tasks_reminder.png)

### 🔹 MySQL Tables in Use  
![DB Preview](mysql_schema_preview.png)

---

## 🔁 Full Project Workflow (Step-by-Step)

This section breaks down how everything works behind the scenes:

### 🧱 Step 1: Set Up MySQL Database
- Created a MySQL database: `simple_crm`
- Designed schema with 5 core tables: `contacts`, `interactions`, `deals`, `tasks`, and `users`
- Inserted sample data using SQL scripts  
> ✅ File: `schema.sql`

---

### 🐍 Step 2: Connect MySQL to Python (with Pandas) and Automate Task Reminder Emails (Daily)
- Used `PyMySQL` to connect Python to the MySQL database
- Ran SQL queries inside Python using `pandas.read_sql()`
- Pulled live data into DataFrames for tasks, deals, and contacts
- Script checks for tasks due **tomorrow**
- Sends personalized Gmail emails using `smtplib` and `email.mime`
- Secured with Gmail App Password (not real password)
- Can be scheduled using **Windows Task Scheduler**

> ✅ File: `send_reminders.py`

---

### 🌐 Step 4: Build a Web Dashboard using Streamlit
- Created a dashboard with tabs for:
  - Contacts 📇
  - Tasks 📋
  - Deals 💼
  - Email Reminders 📤
- Users can:
  - View all data live from MySQL
  - Mark tasks as completed
  - Trigger reminders manually

> ✅ File: `crm_dashboard.py`

---

## 📅 Automation Setup (Scheduling the Script)

- Script (`send_reminders.py`) is scheduled to run daily using **Windows Task Scheduler**
- Runs silently to send emails for tasks due the next day
- No manual input needed after setup

---

## 🙋‍♂️ Author

**Victor Atubeh**  
_Data Analyst with skills in Python, SQL, and Process Automation_

🔗 https://www.linkedin.com/in/victor-atubeh-ba9825297/
---

> 💡 _Passwords and credentials are not included in the public repo. Replace placeholders with your own secure info._
