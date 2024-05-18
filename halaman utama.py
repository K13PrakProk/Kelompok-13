from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def halaman_utama():
    #window1.destroy()
    window3 = tk.Tk()
    window3.title("Pemilihan Resto")
    window3.geometry("1200x675")
    window3.configure(bg="black")
    window3.resizable(True, True)

    frame = Frame(window3, width=150, height=225, bg="white")
    frame.place(x=200,y=100)
    Button(frame, width=20, height=2, text="MCD", fg="black", bg="yellow").place(x=0,y=185)
    img = Image.open("mcd.jpg")
    img = img.resize((185, 185))
    img = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=img, bd=0, highlightthickness=0)
    label.image = img
    label.place(x=-17, y=0)

    frame = Frame(window3, width=150, height=225, bg="white")
    frame.place(x=550,y=100)
    Button(frame, width=20, height=2, text="KFC", fg="black", bg="yellow").place(x=0,y=185)
    img = Image.open("kfc.jpg")
    img = img.resize((185, 185))
    img = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=img, bd=0, highlightthickness=0)
    label.place(x=-17, y=0)

    frame = Frame(window3, width=150, height=225, bg="white")
    frame.place(x=900,y=100)
    Button(frame, width=20, height=2, text="A&W", fg="black", bg="yellow").place(x=0,y=185)
    img = Image.open("aw.png")
    img = img.resize((150, 100))
    img = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=img, bd=0, highlightthickness=0)
    label.place(x=0, y=50)

    frame = Frame(window3, width=150, height=225, bg="white")
    frame.place(x=200,y=400)
    Button(frame, width=20, height=2, text="Burger King", fg="black", bg="yellow").place(x=0,y=185)

    frame = Frame(window3, width=150, height=225, bg="white")
    frame.place(x=550,y=400)
    Button(frame, width=20, height=2, text="Yoshinoya", fg="black", bg="yellow").place(x=0,y=185)

    frame = Frame(window3, width=150, height=225, bg="white")
    frame.place(x=900,y=400)
    Button(frame, width=20, height=2, text="Pizza Hut", fg="black", bg="yellow").place(x=0,y=185)

    window3.mainloop()
halaman_utama()