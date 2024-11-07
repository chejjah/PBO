#segisembilan
import turtle

class Myturtle:
    def __init__(self, color,shape):
        self.t = turtle.Turtle()
        self.t.color (color)
        self.t.shape (shape)

    def maju(self,jarak):
        self.t.forward (jarak)
        
    def putar_kiri(self, sudut):
        self.t.left(sudut)

    def buat_segisembilan(self,ukuran):
        for _ in range(9):
            self.maju (ukuran)
            self.putar_kiri(40)

    def selesai (self):
        turtle.done()

turtle1 = Myturtle ("blue", "turtle")
turtle1.buat_segisembilan(90)
turtle1.selesai()