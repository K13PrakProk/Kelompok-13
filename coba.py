import customtkinter as ctk

def halaman_utama():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Halaman Utama")
    
    # Mendapatkan ukuran layar
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Menetapkan ukuran jendela sesuai dengan ukuran layar
    app.geometry(f"{screen_width}x{screen_height}")

    app.mainloop()

# Mulai dengan halaman utama
halaman_utama()