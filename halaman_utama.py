from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def on_label_click(event):
    messagebox.showinfo("Info", "Natahati Kopi clicked!")

def halaman_utama():
    #window1.destroy()
    window3 = tk.Tk()
    window3.title("Pemilihan Resto")
    window3.geometry("1280x720")
    window3.configure(bg="black")
    window3.resizable(True, True)

    label = tk.Label(window3, text="Silahkan Pilih Resto yang Ingin Anda Kunjungi", fg="white", bg="black", font=("Helvetica", 18, "bold"))
    label.place(x=370, y=10)

    # 1
    frame1 = Frame(window3, width=600, height=150, bg="white")
    frame1.place(x=30, y=50)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/logo1.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame1, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame1, text="Natahati Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", on_label_click)

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame1, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame1, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame1, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1368)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'EXCELLENT' 'breakfast cantik'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame1, image=img3, bd=0, highlightthickness=0)
    label3.image = img2
    label3.place(x=480, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Banjarsari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame1, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Punggawan No.6, Punggawan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57132")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 2
    frame1 = Frame(window3, width=600, height=150, bg="white")
    frame1.place(x=30, y=205)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/logo1.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame1, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame1, text="Natahati Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", on_label_click)

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame1, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame1, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame1, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1368)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'EXCELLENT' 'breakfast cantik'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame1, image=img3, bd=0, highlightthickness=0)
    label3.image = img2
    label3.place(x=480, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Banjarsari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame1, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Punggawan No.6, Punggawan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57132")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 3
    frame1 = Frame(window3, width=600, height=150, bg="white")
    frame1.place(x=30, y=360)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/logo1.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame1, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame1, text="Natahati Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", on_label_click)

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame1, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame1, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame1, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1368)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'EXCELLENT' 'breakfast cantik'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame1, image=img3, bd=0, highlightthickness=0)
    label3.image = img2
    label3.place(x=480, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Banjarsari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame1, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Punggawan No.6, Punggawan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57132")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 4
    frame1 = Frame(window3, width=600, height=150, bg="white")
    frame1.place(x=30, y=515)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/logo1.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame1, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame1, text="Natahati Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", on_label_click)

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame1, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame1, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame1, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1368)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'EXCELLENT' 'breakfast cantik'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame1, image=img3, bd=0, highlightthickness=0)
    label3.image = img2
    label3.place(x=480, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Banjarsari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame1, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Punggawan No.6, Punggawan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57132")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 5
    frame1 = Frame(window3, width=600, height=150, bg="white")
    frame1.place(x=650, y=50)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/logo1.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame1, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame1, text="Natahati Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", on_label_click)

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame1, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame1, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame1, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1368)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'EXCELLENT' 'breakfast cantik'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame1, image=img3, bd=0, highlightthickness=0)
    label3.image = img2
    label3.place(x=480, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Banjarsari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame1, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Punggawan No.6, Punggawan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57132")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 6
    frame1 = Frame(window3, width=600, height=150, bg="white")
    frame1.place(x=650, y=205)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/logo1.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame1, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame1, text="Natahati Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", on_label_click)

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame1, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame1, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame1, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1368)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'EXCELLENT' 'breakfast cantik'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame1, image=img3, bd=0, highlightthickness=0)
    label3.image = img2
    label3.place(x=480, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Banjarsari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame1, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Punggawan No.6, Punggawan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57132")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 7
    frame1 = Frame(window3, width=600, height=150, bg="white")
    frame1.place(x=650, y=360)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/logo1.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame1, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame1, text="Natahati Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", on_label_click)

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame1, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame1, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame1, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1368)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'EXCELLENT' 'breakfast cantik'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame1, image=img3, bd=0, highlightthickness=0)
    label3.image = img2
    label3.place(x=480, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Banjarsari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame1, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Punggawan No.6, Punggawan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57132")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    # 8
    frame1 = Frame(window3, width=600, height=150, bg="white")
    frame1.place(x=650, y=515)

    # Menambahkan gambar
    img1 = Image.open("Kelompok-13/logo1.jpg")
    img1 = img1.resize((170, 150))
    img1 = ImageTk.PhotoImage(img1)
    label1 = tk.Label(frame1, image=img1, bd=0, highlightthickness=0)
    label1.image = img1
    label1.place(x=0, y=0)

    # Membuat label yang terlihat seperti teks biasa dan bisa diklik
    label = tk.Label(frame1, text="Natahati Kopi", fg="black", bg="white", cursor="hand2", font=("Arial", 14, "bold"))
    label.place(x=180, y=5)
    label.bind("<Button-1>", on_label_click)

    img2 = Image.open("Kelompok-13/4.5.png")
    img2 = img2.resize((90, 15))
    img2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(frame1, image=img2, bd=0, highlightthickness=0)
    label2.image = img2
    label2.place(x=197, y=30)

    text = Text(frame1, height=1, width=3, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "4,5")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=30)

    text = Text(frame1, height=1, width=6, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "(1368)")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=283, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Kafe • Rp 1-50.000")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=45)

    text = Text(frame1, height=1, width=50, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "_____________________________________________")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=73)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "'EXCELLENT' 'breakfast cantik'")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=65)

    img3 = Image.open("Kelompok-13/jam.png")
    img3 = img3.resize((15, 15))
    img3 = ImageTk.PhotoImage(img3)
    label3 = tk.Label(frame1, image=img3, bd=0, highlightthickness=0)
    label3.image = img2
    label3.place(x=480, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Setiap Hari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=30)

    text = Text(frame1, height=1, width=30, font=("Arial", 8), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "08.00 - 22.00")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=500, y=45)

    text = Text(frame1, height=1, width=30, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Banjarsari")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=95)

    text = Text(frame1, height=3, width=45, font=("Arial", 8, "italic"), bg="white", cursor="arrow", bd=0, highlightthickness=0)
    text.insert(END, "Jl. Punggawan No.6, Punggawan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57132")
    text.config(state=DISABLED)  # Menonaktifkan edit
    text.place(x=185, y=110)

    window3.mainloop()

halaman_utama()