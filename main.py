from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import re
import ctypes

# Set DPI Awareness (untuk menampilkan High DPI)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Membuat atau terhubung ke database
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Membuat tabel 'users' jika belum ada
c.execute('''CREATE TABLE IF NOT EXISTS users
             (email TEXT PRIMARY KEY, password TEXT, full_name TEXT)''')

# Fungsi registrasi
def update_table():
    try:
        c.execute("ALTER TABLE users ADD COLUMN full_name TEXT")
        conn.commit()
    except sqlite3.OperationalError:
        # Jika kolom sudah ada, maka akan terjadi error dan kita bisa mengabaikannya
        pass

# Panggil fungsi ini sekali untuk memperbarui tabel
update_table()

# Fungsi registrasi
def register(email, password, full_name):
    try:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Email tidak valid. Silakan coba lagi.")
            return
        c.execute("INSERT INTO users (email, password, full_name) VALUES (?, ?, ?)", (email, password, full_name))
        conn.commit()
        messagebox.showinfo("Success", "Registrasi berhasil!")
        
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email sudah digunakan. Silakan coba lagi.")

# Fungsi login
def login(email, password):
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    if c.fetchone() is not None:
        messagebox.showinfo("Success", "Login berhasil!")
        # Masukkan logika untuk halaman utama di sini
    else:
        messagebox.showerror("Error", "Email atau password salah.")

def halaman_login():
    global email_entry, password_entry, window1
    window1 = tk.Tk()
    window1.title("Login")
    window1.geometry("1280x720")
    window1.configure(bg="black")
    window1.resizable(True, True)

    heading = tk.Label(window1, text="Sign In", fg="white", bg="black", font=("Montserrat", 23, "bold"))
    heading.place(x=825, y=170)

    email_label = tk.Label(window1, text="Email:", fg="white", bg="black", font=("Arial", 14))
    email_label.place(x=750, y=220)

    email_entry = tk.Entry(window1, width=25, fg="white", border=4, bg="black", font=(11))
    email_entry.place(x=750, y=250)

    password_label = tk.Label(window1, text="Password:", fg="white", bg="black", font=("Arial", 14))
    password_label.place(x=750, y=290)

    password_entry = tk.Entry(window1, width=25, fg="white", border=4, bg="black", font=(11), show="*")
    password_entry.place(x=750, y=320)

    img = Image.open("Kelompok-13/logo1.png")
    img = ImageTk.PhotoImage(img)
    label = tk.Label(window1, image=img, bd=0, highlightthickness=0)
    label.image = img
    label.place(x=150, y=55)

    def toggle_password_login():
        if show_password_login.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    show_password_login = BooleanVar()
    show_password_checkbox_login = Checkbutton(window1, text="Show Password", variable=show_password_login, onvalue=True, offvalue=False, bg="black", fg="white", command=toggle_password_login)
    show_password_checkbox_login.place(x=750, y=350)

    def halaman_register():
        window1.withdraw()  # Sembunyikan window login
        halaman_register_window = tk.Toplevel(window1)
        halaman_register_window.title("Register")
        halaman_register_window.geometry("1280x720")
        halaman_register_window.configure(bg="black")
        halaman_register_window.resizable(True, True)

        heading = tk.Label(halaman_register_window, text="Sign Up", fg="white", bg="black", font=("Montserrat", 23, "bold"))
        heading.place(x=825, y=100)

        full_name_label = tk.Label(halaman_register_window, text="Nama Lengkap:", fg="white", bg="black", font=("Arial", 14))
        full_name_label.place(x=750, y=150)

        global full_name_entry
        full_name_entry = tk.Entry(halaman_register_window, width=25, fg="white", border=4, bg="black", font=(11))
        full_name_entry.place(x=750, y=180)

        email_label = tk.Label(halaman_register_window, text="Email:", fg="white", bg="black", font=("Arial", 14))
        email_label.place(x=750, y=220)

        global email_entry_register
        email_entry_register = tk.Entry(halaman_register_window, width=25, fg="white", border=4, bg="black", font=(11))
        email_entry_register.place(x=750, y=250)

        password_label = tk.Label(halaman_register_window, text="Password:", fg="white", bg="black", font=("Arial", 14))
        password_label.place(x=750, y=290)

        global password_entry_register
        password_entry_register = tk.Entry(halaman_register_window, width=25, fg="white", border=4, bg="black", font=(11), show="*")
        password_entry_register.place(x=750, y=320)

        def toggle_password_register():
            if show_password_register.get():
                password_entry_register.config(show="")
            else:
                password_entry_register.config(show="*")

        show_password_register = BooleanVar()
        show_password_checkbox_register = Checkbutton(halaman_register_window, text="Show Password", variable=show_password_register, onvalue=True, offvalue=False, bg="black", fg="white", command=toggle_password_register)
        show_password_checkbox_register.place(x=750, y=350)

        img = Image.open("Kelompok-13/logo1.png")
        img = ImageTk.PhotoImage(img)
        label = tk.Label(halaman_register_window, image=img, bd=0, highlightthickness=0)
        label.image = img
        label.place(x=105, y=55)

        def back_login():
            halaman_register_window.destroy()
            window1.deiconify()  # Tampilkan kembali window login saat tombol "Back" ditekan

        register_button = tk.Button(halaman_register_window, width=40, height=1, text="Register", fg="white", bg="black", command=process_registration)
        register_button.place(x=750, y=440)

        back_button = tk.Button(halaman_register_window, width=40, height=1, text="Back", fg="white", bg="black", command=back_login)
        back_button.place(x=750, y=470)

    def check_login():
        email_input = email_entry.get()
        password_input = password_entry.get()
        login(email_input, password_input)

    def toggle_password_login():
        if show_password_login.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    login_button = tk.Button(window1, width=40, height=1, text="Login", fg="white", bg="black", command=check_login)
    login_button.place(x=750, y=370)

    def register_info_click(event):
        halaman_register()

    new_info_label = tk.Label(window1, text="Don't have any account? Please register first.", fg="white", bg="black", font=("Arial", 8), cursor="hand2")
    new_info_label.place(x=750, y=405)
    new_info_label.bind("<Button-1>", register_info_click)
    new_info_label.config(font=("Arial", 8, "bold"), fg="red")

    window1.mainloop()

def process_registration():
    new_email = email_entry_register.get()
    new_password = password_entry_register.get()
    new_full_name = full_name_entry.get()
    register(new_email, new_password, new_full_name)

halaman_login()
conn.close()

        
