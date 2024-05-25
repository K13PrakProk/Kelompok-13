import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Restaurant Reservation")
app.geometry("500x600")

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(fill='both', expand=True, padx=20, pady=20)

def add_entry(parent):
    entry = ctk.CTkEntry(parent, height=30, border_width=2, corner_radius=10)
    entry.pack(padx=10, pady=5, fill='x')
    return entry

def choose_table():
    table_window = ctk.CTkToplevel(app)
    table_window.title("Choose Table")
    table_window.geometry("300x400")
    table_window.resizable(False, False)

    def table_selected(table_number):
        table_entry.configure(state='normal')
        table_entry.delete(0, tk.END)
        table_entry.insert(0, f"Table {table_number}")
        table_entry.configure(state='readonly')
        table_window.destroy()

    ctk.CTkLabel(table_window, text="Select a Table:", font=("Arial", 16)).pack(pady=10)

    for i in range(20):
        ctk.CTkButton(table_window, text=f"Table {i+1}", command=lambda i=i: table_selected(i+1),
                      height=30, border_width=2, corner_radius=10).pack(pady=5, padx=10, fill='x')

def submit_reservation():
    name = name_entry.get()
    phone = phone_entry.get()
    seats = seats_entry.get()
    date = f"{int(day_combobox.get()):02d}-{int(month_combobox.get()):02d}-{year_combobox.get()}"
    time = time_entry.get()
    table = table_entry.get()

    if not name or not phone or not seats or not date or not time or not table:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        seats = int(seats)
    except ValueError:
        messagebox.showwarning("Input Error", "Number of seats must be a number!")
        return

    show_payment_page(name, phone, seats, date, time, table)

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
            ctk.CTkButton(payment_options_frame, text=option, command=lambda opt=option: show_account_form(opt),
                          height=30, border_width=2, corner_radius=10).pack(anchor='center', padx=20, pady=5)

    for method in payment_methods:
        ctk.CTkButton(payment_methods_frame, text=method, command=lambda m=method: show_payment_options(m),
                      height=30, border_width=2, corner_radius=10).pack(anchor='center', padx=20, pady=5)

    payment_options_frame = ctk.CTkFrame(frame, corner_radius=10)
    payment_options_frame.pack(padx=10, pady=5, fill='x')

    back_button = ctk.CTkButton(frame, text="Back", command=show_reservation_page, height=30, border_width=2, corner_radius=10)
    back_button.pack(padx=10, pady=20, side='bottom')

    frame.pack(fill='both', expand=True)

def show_account_form(option):
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
        show_success_page()

    submit_button = ctk.CTkButton(frame, text="Submit", command=submit_payment, height=30, border_width=2, corner_radius=10)
    submit_button.pack(padx=10, pady=20)

    back_button = ctk.CTkButton(frame, text="Back", command=show_payment_page, height=30, border_width=2, corner_radius=10)
    back_button.pack(padx=10, pady=20, side='bottom')

    frame.pack(fill='both', expand=True)

def show_success_page():
    for widget in frame.winfo_children():
        widget.destroy()

    reservation_details = (f"Name: {name_entry.get()}\n"
                           f"Phone: {phone_entry.get()}\n"
                           f"Number of Seats: {seats_entry.get()}\n"
                           f"Date: {int(day_combobox.get()):02d}-{int(month_combobox.get()):02d}-{year_combobox.get()}\n"
                           f"Time: {time_entry.get()}\n"
                           f"Table: {table_entry.get()}")

    details_frame = ctk.CTkFrame(frame, corner_radius=10)
    details_frame.pack(padx=10, pady=5, fill='x', expand=True)

    ctk.CTkLabel(details_frame, text="Reservation Details", font=("Arial", 14, "bold")).pack(padx=10, pady=5)
    ctk.CTkLabel(details_frame, text=reservation_details, justify='left').pack(padx=10, pady=5)

    ctk.CTkLabel(frame, text="Reservasi Anda Berhasil", font=("Arial", 20, "bold")).pack(padx=10, pady=20)

    frame.pack(fill='both', expand=True)

def show_reservation_page():
    for widget in frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(frame, text="Nama Lengkap", font=("Arial", 14)).pack(padx=10, pady=5)
    global name_entry
    name_entry = add_entry(frame)

    ctk.CTkLabel(frame, text="Nomor Handphone", font=("Arial", 14)).pack(padx=10, pady=5)
    global phone_entry
    phone_entry = add_entry(frame)

    ctk.CTkLabel(frame, text="Jumlah kursi", font=("Arial", 14)).pack(padx=10, pady=5)
    global seats_entry
    seats_entry = add_entry(frame)

    ctk.CTkLabel(frame, text="Tanggal Pemesanan", font=("Arial", 14)).pack(padx=10, pady=5)
    date_frame = ctk.CTkFrame(frame, corner_radius=10)
    date_frame.pack(pady=5)
    days = [str(day) for day in range(1, 32)]
    months = [str(month) for month in range(1, 13)]
    years = [str(year) for year in range(2023, 2031)]

    global day_combobox, month_combobox, year_combobox
    day_combobox = ctk.CTkComboBox(date_frame, values=days, width=50)
    day_combobox.pack(side='left', padx=5)
    month_combobox = ctk.CTkComboBox(date_frame, values=months, width=50)
    month_combobox.pack(side='left', padx=5)
    year_combobox = ctk.CTkComboBox(date_frame, values=years, width=70)
    year_combobox.pack(side='left', padx=5)

    ctk.CTkLabel(frame, text="Waktu Pemesanan (HH:MM)", font=("Arial", 14)).pack(padx=10, pady=5)
    global time_entry
    time_entry = add_entry(frame)

    ctk.CTkLabel(frame, text="Pilih Meja", font=("Arial", 14)).pack(padx=10, pady=5)
    global table_entry
    table_entry = ctk.CTkEntry(frame, state='readonly', height=30, border_width=2, corner_radius=10)
    table_entry.pack(padx=10, pady=5, fill='x')

    choose_table_button = ctk.CTkButton(frame, text="Pilih Meja", command=choose_table, height=30, border_width=2, corner_radius=10)
    choose_table_button.pack(padx=10, pady=5)

    submit_button = ctk.CTkButton(frame, text="Submit", command=submit_reservation, height=30, border_width=2, corner_radius=10)
    submit_button.pack(padx=10, pady=20)

    frame.pack(fill='both', expand=True)

show_reservation_page()
app.mainloop()
