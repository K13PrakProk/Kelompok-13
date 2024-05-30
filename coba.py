import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import sqlite3

def choose_table():
        #occupied_tables = get_occupied_tables()
        table_window = ctk.CTkToplevel(app)
        table_window.title("Choose Table")
        table_window.geometry("1280x720")
        table_window.resizable(False, False)
        table_window.transient(app)  # Make this window modal
        table_window.grab_set()
        table_window.state('zoomed')

        #def table_selected(table_number):
            #table_entry.configure(state='normal')
            #table_entry.delete(0, tk.END)
            #table_entry.insert(0, f"Table {table_number}")
            #table_entry.configure(state='readonly')
            #table_window.destroy()

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
                            state=button_state, height=30, border_width=2, corner_radius=10).pack(side='left', padx=5, pady=5)