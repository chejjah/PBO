import tkinter as tk

# Kelas induk Animal
class Animal:
    def make_sound(self):
        return "Some sound"
    
# Kelas turunan Bird 
class Bird(Animal):
    def make_sound(self):
        return "Tweet tweet"
    
# Kelas turunan Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof woof"
    
# Kelas turunan Cat (Hewan tambahan 1)
class Lion(Animal):
    def make_sound(self):
        return "Meow Meow"
    
# Kelas turunan Cow (Hewan tambahan 2)
class Pig(Animal):
    def make_sound(self):
        return "Moo Moo"

# Fungsi untuk menampilkan suara berdasarkan jenis hewan yang dipilih
def show_sound(animal):
    label_result.config(text=animal.make_sound())

# Membangun jendela utama menggunakan Tkinter
root = tk.Tk()
root.title("Polimorfisme di Tkinter")

# Label untuk menampilkan hasil suara 
label_result = tk.Label(root, text="Klik salah satu tombol untuk mendengar suara hewan.", font=("Arial", 14))
label_result.pack(pady=20)

# Tombol untuk memilih Burung
button_bird = tk.Button(root, text="Burung", font=("Arial", 12), 
                        command=lambda: show_sound(Bird()),
                        width=15)
button_bird.pack(pady=10)

# Tombol untuk memilih Anjing
button_dog = tk.Button(root, text="Anjing", font=("Arial", 12), 
                       command=lambda: show_sound(Dog()),
                       width=15)
button_dog.pack(pady=10)

# Tombol untuk memilih Kucing
button_lion = tk.Button(root, text="Kucing", font=("Arial", 12), 
                        command=lambda: show_sound(Lion()),
                        width=15)
button_lion.pack(pady=10)

# Tombol untuk memilih Sapi
button_pig = tk.Button(root, text="Sapi", font=("Arial", 12), 
                       command=lambda: show_sound(Pig()),
                       width=15)
button_pig.pack(pady=10)

# Tombol untuk memilih Hewan Umum
button_animal = tk.Button(root, text="Hewan Umum", font=("Arial", 12), 
                          command=lambda: show_sound(Animal()),
                          width=15)
button_animal.pack(pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
