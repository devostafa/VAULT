import tkinter as tk
from tkinter import filedialog
from services.encrypt import encrypt
from services.decrypt import decrypt
import art

gui = tk.Tk()
gui.title("VAULT")

default_font = "Arial"
font_size_default = 10

header_frame = tk.Frame(gui).pack()
header_title = tk.Label(header_frame, text=art.text2art("VAULT"), font=("Courier", 14), pady=20).pack()

mode_var = tk.IntVar(value=1)  # 1 for Encrypt, 2 for Decrypt

def toggle_mode():
    if mode_var.get() == 1:
        mode_var.set(2)
        submit_button.config(text="Decrypt")
    else:
        mode_var.set(1)
        submit_button.config(text="Encrypt")

toggle_vault = tk.Button(
    header_frame,
    text="Toggle Vault Mode",
    command=toggle_mode).pack()

#--------------------- Key and Output Inputs ---------------------#
body_frame = tk.Frame(gui)
body_frame.pack()

inputs_frame = tk.Frame(body_frame)
inputs_frame.pack(pady=20)

key_frame = tk.Frame(inputs_frame)
key_frame.pack()
key_label = tk.Label(key_frame, text="Key ", font=(default_font, font_size_default))
key_label.pack(side=tk.LEFT)
key_entry = tk.Entry(key_frame, font=(default_font, font_size_default))
key_entry.pack(side=tk.RIGHT)

def select_output_folder():
    folder = filedialog.askdirectory(title="Select Output Folder")
    if folder:
        output_path.set(folder)

output_dir_frame = tk.Frame(inputs_frame)
output_dir_frame.pack(pady=10)

output_path = tk.StringVar(value="")
output_label = tk.Label(output_dir_frame, text="Output Dir ", font=(default_font, font_size_default))
output_label.pack(side=tk.LEFT)
output_input = tk.Entry(output_dir_frame, textvariable=output_path, font=(default_font, font_size_default))
output_input.pack(side=tk.LEFT, pady=10)
output_entry = tk.Button(output_dir_frame, text="Select", command = select_output_folder, font=(default_font, font_size_default)) # Selectable folder path
output_entry.pack(side=tk.LEFT, pady=4) 

#--------------------- Input Files Selection ---------------------#
files_input_frame = tk.Frame(body_frame)
files_input_frame.pack()

selected_files = []

def select_input_files():
    global selected_files
    files = filedialog.askopenfiles(title="Select Files")
    if files:
        selected_files = [f.name for f in files]
        files_entry.delete("1.0", tk.END)
        files_entry.insert("1.0", "\n".join(selected_files))
        submit_button.config(bg="green")

files_interactive_frame = tk.Frame(files_input_frame)
files_interactive_frame.pack(pady=10)

files_label = tk.Label(files_interactive_frame, text="Input Files ", font=(default_font, font_size_default))
files_label.pack(side=tk.LEFT)

files_browse_button = tk.Button(files_interactive_frame, text="Select Files", command=select_input_files)
files_browse_button.pack(side=tk.RIGHT)

files_entry = tk.Text(files_input_frame, font=(default_font, font_size_default), width=50, height=10)
files_entry.pack()

#--------------------- Submit ---------------------#
submit_frame = tk.Frame(body_frame)
submit_frame.pack(pady=20)

def submit_action():
    key = key_entry.get()
    output_dir = output_path.get()
    if mode_var.get() == 1:
        encrypt(key, output_dir, selected_files)
    else:
        decrypt(key, output_dir, selected_files)

submit_button = tk.Button(submit_frame, text="Encrypt", command=submit_action, font=(default_font, font_size_default, "bold"), bd=0, padx=10, pady=5, bg="green", fg="white")
submit_button.pack()

gui.mainloop()