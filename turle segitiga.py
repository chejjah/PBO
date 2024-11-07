import turtle
# Definisi kelas SegitigaTurtle
class SegitigaTurtle:
    # Constructor untuk inisialisasi turtle
    def __init__(self):
        self.t = turtle.Turtle()

    # Method untuk menggambar segitiga
    def gambar_segitiga(self, panjang_sisi):
        for _ in range(3):
            self.t.forward(panjang_sisi)  # Gerak maju
            self.t.left(120)  # Putar 120 derajat ke kiri

    # Method untuk menutup layar turtle saat selesai
    def selesai(self):
        turtle.done()

# Membuat objek dari kelas SegitigaTurtle
segitiga = SegitigaTurtle()

# Menggambar segitiga dengan panjang sisi 100
segitiga.gambar_segitiga(100)

# Menyelesaikan gambar
segitiga.selesai()
