import tkinter as tk
from tkinter import messagebox

# Kelas BankAccount
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private Attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Invalid deposit amount")
    def reset_balance(self):
        self.__balance = 0  # Mengatur saldo menjadi 0

# Fungsi untuk menambah saldo
def add_balance():
    try:
        amount = entry_amount.get()
        if not amount.strip():  # Cek input kosong
            raise ValueError("Masukkan jumlah deposit!")
        amount = int(amount)
        account.deposit(amount)
        label_balance.config(text=f"Balance: {account.get_balance()}")
        entry_amount.delete(0, tk.END)  # Membersihkan input setelah deposit berhasil
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Fungsi untuk mereset input dan saldo
def reset_input():
    entry_amount.delete(0, tk.END)  # Menghapus isi input
    account.reset_balance()  # Mengatur saldo menjadi 0
    label_balance.config(text=f"Balance: {account.get_balance()}")  # Memperbarui tampilan saldo

# GUI Tkinter
root = tk.Tk()
root.title("Data Hiding in BankAccount")

account = BankAccount()

# Frame utama
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Label saldo
label_balance = tk.Label(frame, text=f"Balance: {account.get_balance()}", font=("Arial", 12))
label_balance.pack(pady=10)

# Entry untuk jumlah deposit
entry_amount = tk.Entry(frame, font=("Arial", 10), width=20)
entry_amount.pack(pady=5)

# Frame untuk tombol
button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

# Tombol deposit
button_deposit = tk.Button(button_frame, text="Deposit", command=add_balance, width=10)
button_deposit.pack(side=tk.LEFT, padx=5)

# Tombol reset
button_reset = tk.Button(button_frame, text="Reset", command=reset_input, width=10)
button_reset.pack(side=tk.LEFT, padx=5)

# Menjalankan aplikasi
root.mainloop()
