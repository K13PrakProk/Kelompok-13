from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def window():
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
        halaman_order()

    order_button = tk.Button(frame1, text="Order", command=proceed_to_order, fg="black", bg="orange", font=("Arial", 14, "bold"))
    order_button.place(x=200, y=15)

    def proceed_to_order():
        window_resto1.destroy()
        halaman_reservasi()

    window_resto1.mainloop()

window()
