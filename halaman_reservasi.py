import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import sqlite3

# Create the database and reservation table
conn = sqlite3.connect('reservations.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    seats INTEGER,
    date TEXT,
    time TEXT,
    table_number INTEGER,
    payment_method TEXT,
    name_account TEXT,
    account_number TEXT
    restaurant_name TEXT,
    dp_amount REAL
)
''')
conn.commit()

def halaman_order():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Restaurant Reservation")
    app.geometry("1280x720")

    frame = ctk.CTkFrame(app, corner_radius=15)
    frame.pack(fill='both', expand=True, padx=20, pady=20)

    def add_entry_with_placeholder(parent, placeholder):
        entry = ctk.CTkEntry(parent, height=30, border_width=2, corner_radius=10)
        entry.pack(padx=10, pady=5, fill='x')
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event: on_focus_in(event, placeholder))
        entry.bind("<FocusOut>", lambda event: on_focus_out(event, placeholder))
        return entry

    def on_focus_in(event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, tk.END)
            event.widget.config(fg='black')

    def on_focus_out(event, placeholder):
        if not event.widget.get():
            event.widget.insert(0, placeholder)
            event.widget.config(fg='grey')

    def get_occupied_tables():
        cursor.execute('SELECT table_number FROM reservations')
        return {row[0] for row in cursor.fetchall()}

    def choose_table():
        occupied_tables = get_occupied_tables()
        table_window = ctk.CTkToplevel(app)
        table_window.title("Choose Table")
        table_window.geometry("1280x720")
        table_window.resizable(False, False)

        def table_selected(table_number):
            table_entry.configure(state='normal')
            table_entry.delete(0, tk.END)
            table_entry.insert(0, f"Table {table_number}")
            table_entry.configure(state='readonly')
            table_window.destroy()

        ctk.CTkLabel(table_window, text="Select a Table:", font=("Arial", 16)).pack(pady=10)
        
        table_frame = ctk.CTkFrame(table_window)
        table_frame.pack(pady=5, padx=5, fill='both', expand=True)

        for row in range(5):
            row_frame = ctk.CTkFrame(table_frame)
            row_frame.pack(fill='x')
            for col in range(4):
                table_number = row * 4 + col + 1
                button_state = "normal" if table_number not in occupied_tables else "disabled"
                ctk.CTkButton(row_frame, text=f"Table {table_number}", command=lambda tn=table_number: table_selected(tn),
                            state=button_state, height=30, border_width=2, corner_radius=10).pack(side='left', padx=5, pady=5)

    def submit_reservation():
        name = name_entry.get()
        phone = phone_entry.get()
        seats = seats_entry.get()
        date = f"{int(day_combobox.get()):02d}-{int(month_combobox.get()):02d}-{year_combobox.get()}"
        time = f"{hour_combobox.get()}:{minute_combobox.get()}"
        table = table_entry.get()

        if not name or name == "Name" or not phone or phone == "Phone Number" or not seats or seats == "Number of Seats" or not date or not time or not table:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            seats = int(seats)
        except ValueError:
            messagebox.showwarning("Input Error", "Number of seats must be a number!")
            return

        table_number = int(table.split()[1])
        cursor.execute('SELECT * FROM reservations WHERE table_number = ? AND date = ? AND time = ?', (table_number, date, time))
        if cursor.fetchone():
            messagebox.showwarning("Input Error", "Table is already reserved for the selected date and time!")
            return

        show_payment_page(name, phone, seats, date, time, table_number)

    def show_payment_page(name, phone, seats, date, time, table):
        for widget in frame.winfo_children():
            widget.destroy()

        reservation_details = (f"Name: {name}\n"
                            f"Phone: {phone}\n"
                            f"Number of Seats: {seats}\n"
                            f"Date: {date}\n"
                            f"Time: {time}\n"
                            f"Table: {table}")

        details_frame = ctk.CTkFrame(frame, corner_radius=10)
        details_frame.pack(padx=10, pady=5, fill='x', expand=True)

        ctk.CTkLabel(details_frame, text="Reservation Details", font=("Arial", 14, "bold")).pack(padx=10, pady=5)
        ctk.CTkLabel(details_frame, text=reservation_details, justify='left').pack(padx=10, pady=5)

        ctk.CTkLabel(frame, text="Choose Payment Method", font=("Arial", 14)).pack(padx=10, pady=5)

        payment_methods_frame = ctk.CTkFrame(frame, corner_radius=10)
        payment_methods_frame.pack(padx=10, pady=5, fill='x', expand=True)

        payment_methods = ["QRIS", "E-Wallet", "Bank Transfer"]
        payment_method = tk.StringVar(value=payment_methods[0])

        def show_payment_options(method):
            for widget in payment_options_frame.winfo_children():
                widget.destroy()

            if method == "E-Wallet":
                options = ["ShopeePay", "GoPay", "Dana", "OVO"]
            elif method == "Bank Transfer":
                options = ["BNI", "BRI", "BCA", "Mandiri", "BSI"]
            else:
                options = []

            for option in options:
                ctk.CTkButton(payment_options_frame, text=option, command=lambda opt=option: show_account_form(opt, name, phone, seats, date, time, table, method),
                            height=30, border_width=2, corner_radius=10).pack(anchor='center', padx=20, pady=5)

        for method in payment_methods:
            ctk.CTkButton(payment_methods_frame, text=method, command=lambda m=method: show_payment_options(m),
                        height=30, border_width=2, corner_radius=10).pack(anchor='center', padx=20, pady=5)

        payment_options_frame = ctk.CTkFrame(frame, corner_radius=10)
        payment_options_frame.pack(padx=10, pady=5, fill='x')

        back_button = ctk.CTkButton(frame, text="Back", command=show_reservation_page, height=30, border_width=2, corner_radius=10)
        back_button.pack(padx=10, pady=20, side='bottom')

        frame.pack(fill='both', expand=True)

    def show_account_form(option, name, phone, seats, date, time, table, payment_method):
        for widget in frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(frame, text=f"Payment with {option}", font=("Arial", 16)).pack(padx=10, pady=5)
        ctk.CTkLabel(frame, text="Name Account").pack(padx=10, pady=5)
        name_account_entry = ctk.CTkEntry(frame, height=30, border_width=2, corner_radius=10)
        name_account_entry.pack(padx=10, pady=5, fill='x')

        ctk.CTkLabel(frame, text="Account Number").pack(padx=10, pady=5)
        account_number_entry = ctk.CTkEntry(frame, height=30, border_width=2, corner_radius=10)
        account_number_entry.pack(padx=10, pady=5, fill='x')

        def submit_payment():
            name_account = name_account_entry.get()
            account_number = account_number_entry.get()
            if not name_account or not account_number:
                messagebox.showwarning("Input Error", "All fields are required!")
                return
            create_ticket_page(name, phone, seats, date, time, table, payment_method, name_account, account_number)

        submit_button = ctk.CTkButton(frame, text="Print e-Ticket", command=submit_payment, height=30, border_width=2, corner_radius=10)
        submit_button.pack(padx=10, pady=20)

        back_button = ctk.CTkButton(frame, text="Back", command=lambda: show_payment_page(name, phone, seats, date, time, table), height=30, border_width=2, corner_radius=10)
        back_button.pack(padx=10, pady=20, side='bottom')

        frame.pack(fill='both', expand=True)

    def create_ticket_page(name, phone, seats, date, time, table, payment_method, name_account, account_number):
        cursor.execute('''
            INSERT INTO reservations (name, phone, seats, date, time, table_number, payment_method, name_account, account_number)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, phone, seats, date, time, table, payment_method, name_account, account_number))
        conn.commit()

        ticket_details = (f"--- E-Ticket ---\n\n"
                        f"Name: {name}\n"
                        f"Phone: {phone}\n"
                        f"Number of Seats: {seats}\n"
                        f"Date: {date}\n"
                        f"Time: {time}\n"
                        f"Table: {table}\n"
                        f"Payment Method: {payment_method}\n"
                        f"Account Name: {name_account}\n"
                        f"Account Number: {account_number}")

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>e-Ticket</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 20px;
                }}
                .ticket {{
                    border: 1px solid #000;
                    padding: 20px;
                    border-radius: 10px;
                }}
                h2 {{
                    margin-top: 0;
                }}
            </style>
        </head>
        <body>
            <div class="ticket">
                <h2>Restaurant e-Ticket</h2>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Number of Seats:</strong> {seats}</p>
                <p><strong>Date:</strong> {date}</p>
                <p><strong>Time:</strong> {time}</p>
                <p><strong>Table:</strong> {table}</p>
                <p><strong>Payment Method:</strong> {payment_method}</p>
                <p><strong>Account Name:</strong> {name_account}</p>
                <p><strong>Account Number:</strong> {account_number}</p>
            </div>
        </body>
        </html>
        """

        file_path = os.path.join(os.getcwd(), "e_ticket.html")
        with open(file_path, 'w') as file:
            file.write(html_content)

        webbrowser.open(f"file://{file_path}")

        # Adding a button for making a new reservation
        new_reservation_button = ctk.CTkButton(frame, text="Make a New Reservation", command=show_reservation_page, height=30, border_width=2, corner_radius=10)
        new_reservation_button.pack(padx=10, pady=20)

    def show_reservation_page():
        for widget in frame.winfo_children():
            widget.destroy()

        global name_entry, phone_entry, seats_entry, day_combobox, month_combobox, year_combobox, hour_combobox, minute_combobox, table_entry

        ctk.CTkLabel(frame, text="Make a Reservation", font=("Arial", 20)).pack(padx=10, pady=20)

        name_entry = add_entry_with_placeholder(frame, "Name")
        phone_entry = add_entry_with_placeholder(frame, "Phone Number")
        seats_entry = add_entry_with_placeholder(frame, "Number of Seats")

        ctk.CTkLabel(frame, text="Date").pack(padx=10, pady=5)
        date_frame = ctk.CTkFrame(frame)
        date_frame.pack(pady=5)
        
        day_combobox = ctk.CTkComboBox(date_frame, values=[str(i).zfill(2) for i in range(1, 32)], width=50)
        day_combobox.pack(side='left', padx=5)
        month_combobox = ctk.CTkComboBox(date_frame, values=[str(i).zfill(2) for i in range(1, 13)], width=50)
        month_combobox.pack(side='left', padx=2)
        year_combobox = ctk.CTkComboBox(date_frame, values=[str(i) for i in range(2024, 2030)], width=60)
        year_combobox.pack(side='left', padx=2)

        ctk.CTkLabel(frame, text="Time").pack(padx=10, pady=5)
        time_frame = ctk.CTkFrame(frame)
        time_frame.pack(pady=5)
        
        hour_combobox = ctk.CTkComboBox(time_frame, values=[str(i).zfill(2) for i in range(0, 24)], width=50)
        hour_combobox.pack(side='left', padx=2)
        minute_combobox = ctk.CTkComboBox(time_frame, values=[str(i).zfill(2) for i in range(0, 60)], width=50)
        minute_combobox.pack(side='left', padx=2)

        table_entry = add_entry_with_placeholder(frame, "Table")
        table_entry.configure(state='readonly')
        choose_table_button = ctk.CTkButton(frame, text="Choose Table", command=choose_table, height=30, border_width=2, corner_radius=10)
        choose_table_button.pack(pady=5)

        submit_button = ctk.CTkButton(frame, text="Submit Reservation", command=submit_reservation, height=30, border_width=2, corner_radius=10)
        submit_button.pack(pady=20)

        frame.pack(fill='both', expand=True)

    show_reservation_page()

    app.mainloop()

halaman_order()
