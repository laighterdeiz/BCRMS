import customtkinter as ctk
from backend.db_connect import connect_to_db, initialize_database
from frontend.login import show_login_screen
from frontend.dashboard import show_dashboard

db_path = "database/crime_system.db"
sql_script_path = "database/Tables.sql"

initialize_database(db_path, sql_script_path)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app .title("Barangay Crime Record Management System")
app.geometry("950x650")
app.minsize(780, 560)

def on_login_success(user_id, role):
    print(f"Login successful! User ID: {user_id}, Role: {role}")
    show_dashboard(app, user_id, role, on_logout=lambda: show_login_screen(app, on_login_success))
show_login_screen(app, on_login_success)

app.mainloop()
