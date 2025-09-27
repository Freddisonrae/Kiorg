
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from ..qr import generator


def run_gui():
    mainwindow = tk.Tk()
    mainwindow.title("Noten-Qr Generator")

    # Eingabefelder
    tk.Label(mainwindow, text="Titel").grid(row=0, column=0)
    title_entry = tk.Entry(mainwindow)
    title_entry.grid(row=0, column=1)

    tk.Label(mainwindow, text="Komponist").grid(row=1, column=0)
    composer_entry = tk.Entry(mainwindow)
    composer_entry.grid(row=1, column=1)

    tk.Label(mainwindow, text="Art der Musik").grid(row=2, column=0)
    art_Music_entry = tk.Entry(mainwindow)
    art_Music_entry.grid(row=2, column=1)

    # Label für QR-Code
    qr_label = tk.Label(mainwindow)
    qr_label.grid(row=4, column=0, columnspan=2, pady=10)

    def on_generate():
        metadata = {
            "title": title_entry.get(),
            "composer": composer_entry.get(),
            "art": art_Music_entry.get()
        }
        img = generator.generate_qr(metadata)

        # Für Tkinter konvertieren
        img = img.resize((200, 200))
        qr_photo = ImageTk.PhotoImage(img)
        qr_label.config(image=qr_photo)
        qr_label.image = qr_photo  # Referenz speichern!

    # Button
    tk.Button(mainwindow, text="QR-Code erstellen", command=on_generate).grid(row=3, column=0, columnspan=2, pady=10)

    mainwindow.mainloop()
