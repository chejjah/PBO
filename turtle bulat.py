import turtle

class Myturtle:
    def __init__(self, color, shape):
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.shape(shape)
        
    def bulat(self, ukuran):
        for _ in range(3):
            self.t.circle(150)

    def selesai(self):
        turtle.done()

turtle1 = Myturtle("purple","turtle")
turtle1.bulat(150)
turtle1.selesai 