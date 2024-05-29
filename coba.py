import csv
import re
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Nama file CSV yang akan digunakan
csv_file = 'user_data.csv'

# Fungsi untuk menambahkan header ke file CSV jika belum ada
def initialize_csv():
    try:
        with open(csv_file, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password', 'email', 'nama_lengkap'])
    except FileExistsError:
        pass  # File sudah ada, lanjutkan saja

# Panggil fungsi ini sekali untuk membuat file CSV dan header-nya jika belum ada
initialize_csv()

# Fungsi registrasi
def register(username, password, email, nama_lengkap):
    try:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Email tidak valid. Silakan coba lagi.")
            return

        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username:
                    messagebox.showerror("Error", "Username sudah digunakan. Silakan coba lagi.")
                    return

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, email, nama_lengkap])
            messagebox.showinfo("Success", "Registrasi berhasil!")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Fungsi login
def login(username, password):
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    messagebox.showinfo("Success", "Login berhasil!")
                    halaman_utama()
                    return
            messagebox.showerror("Error", "Username atau password salah.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

def halaman_utama():
    # Implementasi halaman utama setelah login berhasil
    pass

def halaman_login():
    global username_entry, password_entry, window1
    window1 = tk.Tk()
    window1.title("login")
    window1.geometry("1280x720")
    window1.configure(bg="black")
    window1.resizable(True, True)
    window1.state('zoomed')

    heading = tk.Label(window1, text="Sign In", fg="white", bg="black", font=("Montserrat", 23, "bold"))
    heading.place(x=825, y=170)

    username_label = tk.Label(window1, text="Username:", fg="white", bg="black", font=("Arial", 14))
    username_label.place(x=750, y=220)

    username_entry = tk.Entry(window1, width=25, fg="white", border=4, bg="black", font=(11))
    username_entry.place(x=750, y=250)

    password_label = tk.Label(window1, text="Password:", fg="white", bg="black", font=("Arial", 14))
    password_label.place(x=750, y=290)

    password_entry = tk.Entry(window1, width=25, fg="white", border=4, bg="black", font=(11), show="*")
    password_entry.place(x=750, y=320)

    img = Image.open("Kelompok-13/logo1.png")
    img = ImageTk.PhotoImage(img)
    label = tk.Label(window1, image=img, bd=0, highlightthickness=0)
    label.image = img
    label.place(x=150, y=55)

    def halaman_register():
        window1.destroy()
        window2 = tk.Tk()
        window2.title("register")
        window2.geometry("1280x720")
        window2.configure(bg="black")
        window2.resizable(True, True)
        window2.state('zoomed')

        heading = tk.Label(window2, text="Sign Up", fg="white", bg="black", font=("Montserrat", 23, "bold"))
        heading.place(x=825, y=100)

        new_namalengkap_label = tk.Label(window2, text="Nama Lengkap:", fg="white", bg="black", font=("Arial", 14))
        new_namalengkap_label.place(x=750, y=150)

        global new_namalengkap_entry
        new_namalengkap_entry = tk.Entry(window2, width=25, fg="white", border=4, bg="black", font=(11))
        new_namalengkap_entry.place(x=750, y=180)

        new_username_label = tk.Label(window2, text="Username:", fg="white", bg="black", font=("Arial", 14))
        new_username_label.place(x=750, y=220)

        global new_username_entry
        new_username_entry = tk.Entry(window2, width=25, fg="white", border=4, bg="black", font=(11))
        new_username_entry.place(x=750, y=250)

        new_password_label = tk.Label(window2, text="Password:", fg="white", bg="black", font=("Arial", 14))
        new_password_label.place(x=750, y=290)

        global new_password_entry
        new_password_entry = tk.Entry(window2, width=25, fg="white", border=4, bg="black", font=(11), show="*")
        new_password_entry.place(x=750, y=320)

        new_email_label = tk.Label(window2, text="Email:", fg="white", bg="black", font=("Arial", 14))
        new_email_label.place(x=750, y=360)

        global new_email_entry
        new_email_entry = tk.Entry(window2, width=25, fg="white", border=4, bg="black", font=(11))
        new_email_entry.place(x=750, y=390)

        img = Image.open("Kelompok-13/logo1.png")
        img = ImageTk.PhotoImage(img)
        label = tk.Label(window2, image=img, bd=0, highlightthickness=0)
        label.image = img
        label.place(x=105, y=55)

        def back_login():
            window2.destroy()
            halaman_login()

        register_button = tk.Button(window2, width=40, height=1, text="Register", fg="white", bg="black", command=process_registration)
        register_button.place(x=750, y=440)

        back_button = tk.Button(window2, width=40, height=1, text="Back", fg="white", bg="black", command=back_login)
        back_button.place(x=750, y=470)

        window2.mainloop()

    def check_login():
        username_input = username_entry.get()
        password_input = password_entry.get()
        login(username_input, password_input)

    login_button = tk.Button(window1, width=40, height=1, text="Login", fg="white", bg="black", command=check_login)
    login_button.place(x=750, y=370)

    new_info_label = tk.Label(window1, text="Don't have an account? Please register first.", fg="white", bg="black", font=("Arial", 8))
    new_info_label.place(x=750, y=405)

    signup_button = tk.Button(window1, width=40, height=1, text="Sign Up", fg="white", bg="black", command=halaman_register)
    signup_button.place(x=750, y=430)

    window1.mainloop()

def process_registration():
    new_namalengkap = new_namalengkap_entry.get()
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()
    new_email = new_email_entry.get()  # Fetch email from entry field
    register(new_username, new_password, new_email, new_namalengkap)

halaman_login()
