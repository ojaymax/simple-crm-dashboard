import streamlit as st
import pandas as pd
import pymysql
from datetime import datetime, timedelta

# Database connection
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='simple_crm'
    )

# Fetch data helpers
def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def update_task(task_id):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("UPDATE tasks SET is_completed = TRUE WHERE task_id = %s", (task_id,))
        conn.commit()
    conn.close()

# UI Layout
st.title("📊 Simple CRM Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(["📇 Contacts", "📋 Tasks", "💼 Deals", "📤 Send Reminders"])

with tab1:
    st.subheader("All Contacts")
    contacts = fetch_data("SELECT * FROM contacts")
    st.dataframe(contacts)

with tab2:
    st.subheader("Upcoming Tasks")
    tasks = fetch_data("SELECT * FROM tasks WHERE is_completed = FALSE ORDER BY due_date")
    for _, row in tasks.iterrows():
        st.write(f"📌 **{row.task_description}** due on {row.due_date} for `{row.contact_id}`")
        if st.button(f"Mark as done ✅ (Task ID: {row.task_id})", key=row.task_id):
            update_task(row.task_id)
            st.success("Task marked as completed!")
            st.experimental_rerun()

with tab3:
    st.subheader("Deals In Progress")
    deals = fetch_data("SELECT * FROM deals WHERE status = 'open'")
    st.dataframe(deals)

with tab4:
    st.subheader("📤 Send Reminder Emails for Tasks Due Tomorrow")
    tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    query = """
    SELECT t.task_id, t.task_description, t.due_date, c.name, c.email
    FROM tasks t
    JOIN contacts c ON t.contact_id = c.contact_id
    WHERE t.due_date = %s AND t.is_completed = FALSE
    """
    reminders = fetch_data(query % f"'{tomorrow}'")

    if not reminders.empty:
        st.dataframe(reminders)
        if st.button("Send Reminders Now"):
            # You can plug in the email sending logic here
            st.success("✅ Reminders would be sent (connect your email logic)")
    else:
        st.info("No reminders to send for tomorrow.")
