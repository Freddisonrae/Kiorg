import tkinter as tk

root = tk.Tk()
root.title("Testfenster")
root.geometry("300x200")

tk.Label(root, text="Hallo Tkinter!").pack()

root.mainloop()
