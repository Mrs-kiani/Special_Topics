
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText


# تابع رمزنگاری سزار
def encrypt(plain_text, key):
    result = ""

    for char in plain_text:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + key) % 26 + base)
            result += new_char
        else:
            result += char

    return result


# تابع رمزگشایی سزار
def decrypt(cipher_text, key):
    return encrypt(cipher_text, -key)


# تابع دریافت کلید و رمزنگاری
def do_encrypt():
    try:
        key = int(key_entry.get())
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter your text!")
            return

        result = encrypt(text, key)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer key!")


# تابع دریافت کلید و رمزگشایی
def do_decrypt():
    try:
        key = int(key_entry.get())
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter your text!")
            return

        result = decrypt(text, key)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer key!")


# پاک کردن ورودی و خروجی
def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)


# ساخت پنجره اصلی
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("700x650")
root.configure(bg="#151526")
root.resizable(False, False)


# استایل دکمه ها
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Arial", 11, "bold"),
    padding=10,
    background="#7657D5",
    foreground="white"
)

style.map(
    "TButton",
    background=[("active", "#9479F0")]
)


# عنوان برنامه
title = tk.Label(
    root,
    text="CAESAR CIPHER",
    font=("Arial", 25, "bold"),
    bg="#151526",
    fg="#A78BFA"
)
title.pack(pady=(25, 5))


subtitle = tk.Label(
    root,
    text="Encryption & Decryption System",
    font=("Arial", 11),
    bg="#151526",
    fg="#B8B8CC"
)
subtitle.pack(pady=5)


# بخش متن ورودی
input_label = tk.Label(
    root,
    text="Enter Your Text:",
    font=("Arial", 12, "bold"),
    bg="#151526",
    fg="white"
)
input_label.pack(anchor="w", padx=55, pady=(20, 5))


input_text = ScrolledText(
    root,
    width=65,
    height=5,
    font=("Arial", 12),
    bg="#25253B",
    fg="white",
    insertbackground="white",
    relief="flat",
    wrap="word"
)
input_text.pack(padx=50, pady=5)


# بخش کلید
key_frame = tk.Frame(root, bg="#151526")
key_frame.pack(pady=20)

key_label = tk.Label(
    key_frame,
    text="Encryption Key:",
    font=("Arial", 12, "bold"),
    bg="#151526",
    fg="white"
)
key_label.pack(side="left", padx=10)

key_entry = tk.Entry(
    key_frame,
    width=12,
    font=("Arial", 13),
    bg="#25253B",
    fg="white",
    insertbackground="white",
    justify="center",
    relief="flat"
)
key_entry.pack(side="left", ipady=7)


# دکمه های عملیات
button_frame = tk.Frame(root, bg="#151526")
button_frame.pack(pady=10)

encrypt_btn = ttk.Button(
    button_frame,
    text="ENCRYPT",
    command=do_encrypt
)
encrypt_btn.pack(side="left", padx=12)

decrypt_btn = ttk.Button(
    button_frame,
    text="DECRYPT",
    command=do_decrypt
)
decrypt_btn.pack(side="left", padx=12)

clear_btn = ttk.Button(
    button_frame,
    text="CLEAR",
    command=clear_all
)
clear_btn.pack(side="left", padx=12)


# بخش نمایش نتیجه
output_label = tk.Label(
    root,
    text="Result:",
    font=("Arial", 12, "bold"),
    bg="#151526",
    fg="white"
)
output_label.pack(anchor="w", padx=55, pady=(20, 5))


output_text = ScrolledText(
    root,
    width=65,
    height=6,
    font=("Arial", 12),
    bg="#25253B",
    fg="#A78BFA",
    insertbackground="white",
    relief="flat",
    wrap="word"
)
output_text.pack(padx=50, pady=5)


# متن پایین برنامه
footer = tk.Label(
    root,
    text="Caesar Cipher Algorithm | Python Project",
    font=("Arial", 9),
    bg="#151526",
    fg="#77778F"
)
footer.pack(pady=15)


# اجرای برنامه
root.mainloop()
