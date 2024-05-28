from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import re
<<<<<<< HEAD
import halaman_reservasi
=======
import ctypes

# Set DPI Awareness (untuk menampilkan High DPI)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
>>>>>>> de1c0f24f6e1ed6278fac01bbdc0daa9190e28fd

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

def halaman_utama():
    def on_label_click_resto1():
        window3.destroy()
        # Buat halaman baru untuk restoran Truntum
        window_resto1 = tk.Tk()
        window_resto1.title("Truntum")
        window_resto1.geometry("1280x1720")
        window_resto1.configure(bg="black")
        window_resto1.resizable(True, True)

        img_bg = Image.open("Kelompok-13/menutruntum.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto1, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto1, width=300, height=70, bg="black")
        frame1.place(x=490, y=610)

        def back_to_previous():
            window_resto1.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto1.destroy()
            halaman_reservasi.halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

    def on_label_click_resto2():
        window3.destroy()
        # Buat halaman baru untuk restoran Kopi Jahat
        window_resto2 = tk.Tk()
        window_resto2.title("Bento Kopi")
        window_resto2.geometry("1280x720")
        window_resto2.configure(bg="black")
        window_resto2.resizable(True, True)

        # Menambahkan gambar background
        img_bg = Image.open("Kelompok-13/menubento.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto2, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto2, width=300, height=70, bg="black")
        frame1.place(x=490, y=610)

        def back_to_previous():
            window_resto2.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto2.destroy()
            halaman_reservasi.halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

    def on_label_click_resto3():
        window3.destroy()
        # Buat halaman baru untuk restoran Cold 'N Brew
        window_resto3 = tk.Tk()
        window_resto3.title("Cold 'N Brew")
        window_resto3.geometry("1280x720")
        window_resto3.configure(bg="black")
        window_resto3.resizable(True, True)

        # Menambahkan gambar background
        img_bg = Image.open("Kelompok-13/menubrew.png")
        img_bg = img_bg.resize((1280,720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto3, image=bg_image, bd=0, highlightthickness=0)
        bg_label.image = bg_image
        bg_label.place(x=0, y=-110)

        label = tk.Label(window_resto3, text="DAFTAR MENU", fg="white", bg="black", font=("Helvetica", 22, "bold"))
        label.place(x=200, y=190)

        frame1 = Frame(window_resto3, width=300, height=70, bg="black")
        frame1.place(x=490, y=610)

        def back_to_previous():
            window_resto3.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto3.destroy()
            halaman_reservasi.halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)


    def on_label_click_resto4():
        window3.destroy()
        # Buat halaman baru untuk restoran Cold 'N Brew
        window_resto4 = tk.Tk()
        window_resto4.title("La Luna Coffee & Eatery")
        window_resto4.geometry("1280x720")
        window_resto4.configure(bg="black")
        window_resto4.resizable(True, True)

        img_bg = Image.open("Kelompok-13/menulaluna.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto4, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto4, width=300, height=70, bg="black")
        frame1.place(x=490, y=610)

        def back_to_previous():
            window_resto4.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto4.destroy()
            halaman_reservasi.halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

    def on_label_click_resto5():
        window3.destroy()
        # Buat halaman baru untuk restoran Cold 'N Brew
        window_resto5 = tk.Tk()
        window_resto5.title("Bukuku Lawas")
        window_resto5.geometry("1280x720")
        window_resto5.configure(bg="black")
        window_resto5.resizable(True, True)

        img_bg = Image.open("Kelompok-13/menubukuku.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto5, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto5, width=300, height=70, bg="black")
        frame1.place(x=490, y=610)

        def back_to_previous():
            window_resto5.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto5.destroy()
            halaman_reservasi.halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

    def on_label_click_resto6():
        window3.destroy()
        # Buat halaman baru untuk restoran Cold 'N Brew
        window_resto6 = tk.Tk()
        window_resto6.title("Almamater Coffee & Eatery")
        window_resto6.geometry("1280x720")
        window_resto6.configure(bg="black")
        window_resto6.resizable(True, True)

        img_bg = Image.open("Kelompok-13/menualmamater.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto6, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto6, width=300, height=70, bg="black")
        frame1.place(x=490, y=610)

        def back_to_previous():
            window_resto6.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto6.destroy()
            halaman_reservasi.halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)
    
    def on_label_click_resto7():
        window3.destroy()
        # Buat halaman baru untuk restoran Cold 'N Brew
        window_resto7 = tk.Tk()
        window_resto7.title("Kopi Konnichiwa")
        window_resto7.geometry("1280x720")
        window_resto7.configure(bg="black")
        window_resto7.resizable(True, True)

        img_bg = Image.open("Kelompok-13/menu.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto7, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto7, width=300, height=70, bg="black")
        frame1.place(x=490, y=610)

        def back_to_previous():
            window_resto7.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto7.destroy()
            halaman_reservasi.halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

    def on_label_click_resto8():
        window3.destroy()
        # Buat halaman baru untuk restoran Cold 'N Brew
        window_resto8 = tk.Tk()
        window_resto8.title("Natahati Kopi")
        window_resto8.geometry("1280x720")
        window_resto8.configure(bg="black")
        window_resto8.resizable(True, True)

        img_bg = Image.open("Kelompok-13/menunatahati.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto8, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto8, width=300, height=70, bg="black")
        frame1.place(x=490, y=610)

        def back_to_previous():
            window_resto8.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto8.destroy()
            halaman_reservasi.halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

    window1.destroy()
    window3 = tk.Tk()
    window3.title("Pemilihan Resto")
    window3.geometry("1280x720")
    window3.configure(bg="black")
    window3.resizable(True, True)

    label = tk.Label(window3, text="Silahkan Pilih Resto yang Ingin Anda Kunjungi", fg="white", bg="black", font=("Helvetica", 18, "bold"))
    label.place(x=370, y=10)

    # Restoran 1: Truntum
    frame1 = Frame(window3, width=600, height=150, bg="white")
    frame1.place(x=30, y=50)

    # Menambahkan gambar
    img11 = Image.open("Kelompok-13/truntum.jpg")
    img11 = img11.resize((170, 150))
    img11 = ImageTk.PhotoImage(img11)
    label11 = tk.Label(frame1, image=img11, bd=0, highlightthickness=0)
    label11.image = img11
    label11.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame1, text="Truntum", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", lambda event: on_label_click_resto1())

    img12 = Image.open("Kelompok-13/4.5.png")
    img12 = img12.resize((90, 15))
    img12 = ImageTk.PhotoImage(img12)
    label12 = tk.Label(frame1, image=img12, bd=0, highlightthickness=0)
    label12.image = img12
    label12.place(x=197, y=30)

    text = Text(frame1, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame1, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1.126)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Rumah Makan • Rp 25.000-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'Tempatnya so cozy apalagi harga maknanan murah'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img13 = Image.open("Kelompok-13/jam.png")
    img13 = img13.resize((15, 15))
    img13 = ImageTk.PhotoImage(img13)
    label13 = tk.Label(frame1, image=img13, bd=0, highlightthickness=0)
    label13.image = img13
    label13.place(x=480, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Minggu TUTUP")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "11.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jebres")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame1, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Antariksa III, Jebres, Kec. Jebres, Kota Surakarta, Jawa Tengah 57126")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)        


    # Restoran 2: Bento Kopi
    frame2 = Frame(window3, width=600, height=150, bg="white")
    frame2.place(x=30, y=205)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/bento.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame2, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame2, text="Bento Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", lambda event: on_label_click_resto2())     

    img2 = Image.open("Kelompok-13/4.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame2, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame2, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,2")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame2, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(980)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame2, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kedai Kopi • Rp 1-25.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame2, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame2, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'Pelayanan ramah dan kantong pelajar untuk masalah menu'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame2, image=img3, bd=0, highlightthickness=0)
    label3.image = img3
    label3.place(x=480, y=45)

    text = Text(frame2, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame2, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "09.00 - 01.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame2, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jebres")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame2, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Agung Timur No.14, Mojosongo, Kec. Jebres, Kota Surakarta, Jawa Tengah 57181")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # Restoran 3: Cold 'N Brew
    frame3 = Frame(window3, width=600, height=150, bg="white")
    frame3.place(x=30, y=360)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/brew.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame3, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame3, text="Cold 'N Brew", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", lambda event: on_label_click_resto3())

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame3, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame3, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,6")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame3, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(598)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame3, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 25.000-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame3, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame3, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'Tempat nongki kopi depan kampus UNS'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame3, image=img3, bd=0, highlightthickness=0)
    label3.image = img3
    label3.place(x=480, y=45)

    text = Text(frame3, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame3, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "07.00 - 23.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame3, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jebres")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame3, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Ir. Sutami No.104, Pucangsawit, Kec. Jebres, Kota Surakarta, Jawa Tengah 57125")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # Restoran 4 : La Luna Coffee & Eatery
    frame4 = Frame(window3, width=600, height=150, bg="white")
    frame4.place(x=30, y=515)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/luna.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame4, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame4, text="La Luna Coffee & Eatery", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", lambda event: on_label_click_resto4())

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame4, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame4, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,7")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame4, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(167)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame4, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 25.000-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame4, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame4, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'Tempat makan dan nongkrong yg asyik bgt'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame4, image=img3, bd=0, highlightthickness=0)
    label3.image = img3
    label3.place(x=480, y=45)

    text = Text(frame4, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame4, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "10.00 - 00.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame4, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jebres")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame4, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Ir. Sutami No.64, Jebres, Kec. Jebres, Kota Surakarta, Jawa Tengah 57125")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 5 Bukuku Lawas
    frame5 = Frame(window3, width=600, height=150, bg="white")
    frame5.place(x=650, y=50)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/bukuku.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame5, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame5, text="Bukuku Lawas", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", lambda event: on_label_click_resto5())

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame5, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame5, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,6")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame5, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(708)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame5, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-25.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame5, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame5, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'Perfect place untuk semua pecinta buku.'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame5, image=img3, bd=0, highlightthickness=0)
    label3.image = img3
    label3.place(x=480, y=45)

    text = Text(frame5, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame5, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "15.00 - 00.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame5, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jebres")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame5, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Guruh No.26, RT. 01, Ngasinan, Kec. Jebres, Kota Surakarta, Jawa Tengah 57126")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 6 Almamater Coffee & Eatery
    frame6 = Frame(window3, width=600, height=150, bg="white")
    frame6.place(x=650, y=205)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/almamater.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame6, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame6, text="Almamater Coffee & Eatery", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", lambda event: on_label_click_resto6())

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame6, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame6, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,6")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame6, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1.577)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame6, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 25.000-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame6, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame6, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'Coffe shop niat! Kopi enak makanan enak dan beragam'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame6, image=img3, bd=0, highlightthickness=0)
    label3.image = img3
    label3.place(x=480, y=45)

    text = Text(frame6, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame6, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 00.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame6, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jebres")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame6, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Ir. Sutami No.32, Jebres, Kec. Jebres, Kota Surakarta, Jawa Tengah 57126")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 7 Kopi Konnichiwa
    frame7 = Frame(window3, width=600, height=150, bg="white")
    frame7.place(x=650, y=360)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/koniciwa.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame7, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame7, text="Kopi Konnichiwa", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", lambda event: on_label_click_resto7())

    img2 = Image.open("Kelompok-13/5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame7, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame7, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,8")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame7, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(214)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame7, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 25.000-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame7, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame7, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'Kopinya enak, kental dan kerasa bgt kopinya.'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame7, image=img3, bd=0, highlightthickness=0)
    label3.image = img3
    label3.place(x=480, y=45)

    text = Text(frame7, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame7, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "09.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame7, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jebres")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame7, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Ki Hajar Dewantara No.49, Jebres, Kec. Jebres, Kota Surakarta, Jawa Tengah 57126")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 8 Natahati Kopi
    frame8 = Frame(window3, width=600, height=150, bg="white")
    frame8.place(x=650, y=515)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/logo1.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame8, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame8, text="Natahati Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", lambda event: on_label_click_resto8())

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame8, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame8, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame8, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1368)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame8, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame8, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame8, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'EXCELLENT' 'breakfast cantik'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame8, image=img3, bd=0, highlightthickness=0)
    label3.image = img3
    label3.place(x=480, y=45)

    text = Text(frame8, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame8, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame8, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Banjarsari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame8, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Punggawan No.6, Punggawan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57132")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)


    window3.mainloop()
halaman_login()
conn.close()

        
