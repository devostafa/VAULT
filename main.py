import tkinter as tk
from services.encrypt import encrypt
from services.decrypt import decrypt

root = tk.Tk()
root.title("VAULT")
root.geometry("600x800")
root.resizable(True, True)

root.mainloop()
