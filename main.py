from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def halaman_login():
    window1 = tk.Tk()
    window1.title("login")
    window1.geometry("1200x675")
    window1.configure(bg="black")
    window1.resizable(True, True)

    heading = tk.Label(window1, text="Sign In", fg="white", bg="black", font=("Montserrat", 23, "bold"))
    heading.place(x=825, y=205)

    username_label = tk.Label(window1, text="Username:", fg="white", bg="black", font=("Arial", 14))
    username_label.place(x=750, y=270)

    username = tk.Entry(window1, width=25, fg="white", border=4, bg="black", font=(11))
    username.place(x=750, y=300)

    password_label = tk.Label(window1, text="Password:", fg="white", bg="black", font=("Arial", 14))
    password_label.place(x=750, y=350)

    password = tk.Entry(window1, width=25, fg="white", border=4, bg="black", font=(11), show="*")
    password.place(x=750, y=380)

    img = Image.open("Kelompok-13\logo1.png")
    img = ImageTk.PhotoImage(img)
    label = tk.Label(window1, image=img, bd=0, highlightthickness=0)
    label.place(x=105, y=55)

    def halaman_register():
        window1.destroy()
        window2 = tk.Tk()
        window2.title("register")
        window2.geometry("1200x675")
        window2.configure(bg="black")
        window2.resizable(True, True)

        heading = tk.Label(window2, text="Sign Up", fg="white", bg="black", font=("Montserrat", 23, "bold"))
        heading.place(x=825, y=205)

        username_label = tk.Label(window2, text="Username:", fg="white", bg="black", font=("Arial", 14))
        username_label.place(x=750, y=270)

        username = tk.Entry(window2, width=25, fg="white", border=4, bg="black", font=(11))
        username.place(x=750, y=300)

        password_label = tk.Label(window2, text="Password:", fg="white", bg="black", font=("Arial", 14))
        password_label.place(x=750, y=350)

        password = tk.Entry(window2, width=25, fg="white", border=4, bg="black", font=(11), show="*")
        password.place(x=750, y=380)

        img = Image.open("Kelompok-13\logo1.png")
        img = ImageTk.PhotoImage(img)
        label = tk.Label(window2, image=img, bd=0, highlightthickness=0)
        label.place(x=105, y=55)

        def back_login():
            window2.destroy()
            halaman_login()

        login_button = tk.Button(window2, width=40, height=1, text="Login", fg="white", bg="black")
        login_button.place(x=750, y=430)

        back_button = tk.Button(window2, width=40, height=1, text="Back", fg="white", bg="black", command=back_login)
        back_button.place(x=750, y=460)

        window2.mainloop()

    
    def halaman_utama():
        window1.destroy()
        window3 = tk.Tk()
        window3.title("Pemilihan Resto")
        window3.geometry("1200x675")
        window3.configure(bg="black")
        window3.resizable(True, True)

        # MCD
        frame1 = Frame(window3, width=150, height=225, bg="white")
        frame1.place(x=200, y=100)
        Button(frame1, width=20, height=2, text="MCD", fg="black", bg="yellow").place(x=0, y=185)
        img1 = Image.open("Kelompok-13/mcd.jpg")
        img1 = img1.resize((185, 185))
        img1 = ImageTk.PhotoImage(img1)
        label1 = tk.Label(frame1, image=img1, bd=0, highlightthickness=0)
        label1.image = img1
        label1.place(x=-17, y=0)

        # KFC
        frame2 = Frame(window3, width=150, height=225, bg="white")
        frame2.place(x=550, y=100)
        Button(frame2, width=20, height=2, text="KFC", fg="black", bg="yellow").place(x=0, y=185)
        img2 = Image.open("Kelompok-13/kfc.jpg")
        img2 = img2.resize((185, 185))
        img2 = ImageTk.PhotoImage(img2)
        label2 = tk.Label(frame2, image=img2, bd=0, highlightthickness=0)
        label2.image = img2
        label2.place(x=-17, y=0)

        # A&W
        frame3 = Frame(window3, width=150, height=225, bg="white")
        frame3.place(x=900, y=100)
        Button(frame3, width=20, height=2, text="A&W", fg="black", bg="yellow").place(x=0, y=185)
        img3 = Image.open("Kelompok-13/aw.png")
        img3 = img3.resize((150, 100))
        img3 = ImageTk.PhotoImage(img3)
        label3 = tk.Label(frame3, image=img3, bd=0, highlightthickness=0)
        label3.image = img3
        label3.place(x=0, y=50)

        # Burger King
        frame4 = Frame(window3, width=150, height=225, bg="white")
        frame4.place(x=200, y=400)
        Button(frame4, width=20, height=2, text="Burger King", fg="black", bg="yellow").place(x=0, y=185)

        # Yoshinoya
        frame5 = Frame(window3, width=150, height=225, bg="white")
        frame5.place(x=550, y=400)
        Button(frame5, width=20, height=2, text="Yoshinoya", fg="black", bg="yellow").place(x=0, y=185)

        # Pizza Hut
        frame6 = Frame(window3, width=150, height=225, bg="white")
        frame6.place(x=900, y=400)
        Button(frame6, width=20, height=2, text="Pizza Hut", fg="black", bg="yellow").place(x=0, y=185)

        window3.mainloop()

    login_button = tk.Button(window1, width=40, height=1, text="Login", fg="white", bg="black", command=halaman_utama)
    login_button.place(x=750, y=430)

    signup_button = tk.Button(window1, width=40, height=1, text="Sign Up", fg="white", bg="black", command=halaman_register)
    signup_button.place(x=750, y=460)

    window1.mainloop()

halaman_login()
