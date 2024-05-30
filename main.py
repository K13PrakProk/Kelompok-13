from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import re
import customtkinter as ctk
import webbrowser
import os
import  sqlite3

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

def halaman_utama():
    def on_label_click_resto1():
        window3.withdraw()
        # Buat halaman baru untuk restoran Truntum
        window_resto1 = tk.Toplevel(window3)
        window_resto1.title("Truntum")
        window_resto1.geometry("1280x1720")
        window_resto1.configure(bg="black")
        window_resto1.resizable(True, True)
        window_resto1.state('zoomed')

        img_bg = Image.open("Kelompok-13//menutruntum.png")
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
            halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

        window_resto1.mainloop()

    def on_label_click_resto2():
        window3.withdraw()
        window_resto2 = tk.Toplevel(window3)
        window_resto2.title("Bento Kopi")
        window_resto2.geometry("1280x720")
        window_resto2.configure(bg="black")
        window_resto2.resizable(True, True)
        window_resto2.state('zoomed')

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
            halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

        window_resto2.mainloop()

    def on_label_click_resto3():
        window3.withdraw()
        # Buat halaman baru untuk restoran Cold 'N Brew
        window_resto3 = tk.Toplevel(window3)
        window_resto3.title("Cold 'N Brew")
        window_resto3.geometry("1280x720")
        window_resto3.configure(bg="black")
        window_resto3.resizable(True, True)
        window_resto3.state('zoomed')

        # Menambahkan gambar background
        img_bg = Image.open("Kelompok-13/menubrew.png")
        img_bg = img_bg.resize((1280,720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto3, image=bg_image, bd=0, highlightthickness=0)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0)

        frame1 = Frame(window_resto3, width=300, height=70, bg="black")
        frame1.place(x=490, y=620)

        def back_to_previous():
            window_resto3.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto3.destroy()
            halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

        window_resto3.mainloop()


    def on_label_click_resto4():
        window3.withdraw()
        # Buat halaman baru untuk restoran Cold 'N Brew
        window_resto4 = tk.Toplevel(window3)
        window_resto4.title("La Luna Coffee & Eatery")
        window_resto4.geometry("1280x720")
        window_resto4.configure(bg="black")
        window_resto4.resizable(True, True)
        window_resto4.state('zoomed')

        img_bg = Image.open("Kelompok-13/menulaluna.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto4, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto4, width=300, height=70, bg="black")
        frame1.place(x=490, y=600)

        def back_to_previous():
            window_resto4.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto4.destroy()
            halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

        window_resto4.mainloop()

    def on_label_click_resto5():
        window3.withdraw()
        window_resto5 = tk.Toplevel(window3)
        window_resto5.title("Bukuku Lawas")
        window_resto5.geometry("1280x720")
        window_resto5.configure(bg="black")
        window_resto5.resizable(True, True)
        window_resto5.state('zoomed')

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
            halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

        window_resto5.mainloop()

    def on_label_click_resto6():
        window3.withdraw()
        window_resto6 = tk.Toplevel(window3)
        window_resto6.title("Almamater Coffee & Eatery")
        window_resto6.geometry("1280x720")
        window_resto6.configure(bg="black")
        window_resto6.resizable(True, True)
        window_resto6.state('zoomed')

        img_bg = Image.open("Kelompok-13/menualmamater.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto6, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto6, width=300, height=70, bg="black")
        frame1.place(x=490, y=585)

        def back_to_previous():
            window_resto6.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto6.destroy()
            halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

        window_resto6.mainloop()
    
    def on_label_click_resto7():
        window3.withdraw()
        window_resto7 = tk.Toplevel(window3)
        window_resto7.title("Kopi Konnichiwa")
        window_resto7.geometry("1280x720")
        window_resto7.configure(bg="black")
        window_resto7.resizable(True, True)
        window_resto7.state('zoomed')

        img_bg = Image.open("Kelompok-13/menu.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto7, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto7, width=300, height=70, bg="black")
        frame1.place(x=490, y=630)

        def back_to_previous():
            window_resto7.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto7.destroy()
            halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

        window_resto7.mainloop()

    def on_label_click_resto8():
        window3.withdraw()
        window_resto8 = tk.Toplevel(window3)
        window_resto8.title("Natahati Kopi")
        window_resto8.geometry("1280x720")
        window_resto8.configure(bg="black")
        window_resto8.resizable(True, True)
        window_resto8.state('zoomed')

        img_bg = Image.open("Kelompok-13/menunatahati.png")
        img_bg = img_bg.resize((1280, 720))
        bg_image = ImageTk.PhotoImage(img_bg)
        bg_label = tk.Label(window_resto8, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(window_resto8, width=300, height=70, bg="black")
        frame1.place(x=490, y=600)

        def back_to_previous():
            window_resto8.destroy()
            halaman_utama()

        back_button = tk.Button(frame1, text="Back", command=back_to_previous, fg="black", bg="orange", font=("Arial", 14, "bold"))
        back_button.place(x=35, y=15)

        def proceed_to_order():
            window_resto8.destroy()
            halaman_order()

        order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
        order_button.place(x=200, y=15)

        window_resto8.mainloop()

    window1.withdraw()
    window3 = tk.Toplevel(window1)
    window3.title("Pemilihan Resto")
    window3.geometry("1280x720")
    window3.configure(bg="black")
    window3.resizable(True, True)
    window3.state('zoomed')

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
    label2.place(x=202, y=30)

    text = Text(frame2, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,2")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame2, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(980)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=288, y=30)

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
    label2.place(x=198, y=30)

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
    label2.place(x=200, y=30)

    text = Text(frame7, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,8")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame7, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(214)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=288, y=30)

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
    app.state('zoomed')

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
        table_window.transient(app)  # Make this window modal
        table_window.grab_set()
        table_window.state('zoomed')

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
                            state=button_state, height=30, border_width=2, corner_radius=10).pack(side='left', padx=90, pady=45)

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
        
        day_combobox = ctk.CTkComboBox(date_frame, values=[str(i).zfill(2) for i in range(1, 32)], width=60)
        day_combobox.pack(side='left', padx=5)
        month_combobox = ctk.CTkComboBox(date_frame, values=[str(i).zfill(2) for i in range(1, 13)], width=60)
        month_combobox.pack(side='left', padx=2)
        year_combobox = ctk.CTkComboBox(date_frame, values=[str(i) for i in range(2024, 2030)], width=70)
        year_combobox.pack(side='left', padx=2)

        ctk.CTkLabel(frame, text="Time").pack(padx=10, pady=5)
        time_frame = ctk.CTkFrame(frame)
        time_frame.pack(pady=5)
        
        hour_combobox = ctk.CTkComboBox(time_frame, values=[str(i).zfill(2) for i in range(0, 24)], width=60)
        hour_combobox.pack(side='left', padx=2)
        minute_combobox = ctk.CTkComboBox(time_frame, values=[str(i).zfill(2) for i in range(0, 60)], width=60)
        minute_combobox.pack(side='left', padx=2)

        table_entry = add_entry_with_placeholder(frame, "Table")
        table_entry.configure(state='readonly')
        choose_table_button = ctk.CTkButton(frame, text="Choose Table", command=choose_table, height=30, border_width=2, corner_radius=10)
        choose_table_button.pack(pady=5)

        submit_button = ctk.CTkButton(frame, text="Submit Reservation", command=submit_reservation, height=30, border_width=2, corner_radius=10)
        submit_button.pack(pady=20)

        back_button = ctk.CTkButton(frame, text="Back", command=back_to_halaman_utama, height=30, border_width=2, corner_radius=10)
        back_button.pack(padx=30, pady=20)

        frame.pack(fill='both', expand=True)
    def back_to_halaman_utama():
        halaman_utama()
        
    show_reservation_page()

    app.mainloop()

halaman_login()
