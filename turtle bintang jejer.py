import turtle

# create a StarDrawer class to handle the drawing logic
class StarDrawer:
    def __init__(self,x, y, color):
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.color(color)

    # method to darw a single star
    def draw_star(self):
        for _ in range(5):
            self.t.forward(100)
            self.t.right(144)

    # method to move to the next position
    def move_to_next(self, distance):
        self.t.penup()
        self.t.forward(distance)
        self.t.pendown()

    def selesai(self):
        turtle.done()

# initialize screen
screen = turtle.Screen()
screen.bgcolor("white")

# create two turtle objects for drawing
star1 = StarDrawer(-150, 0, 'pink')
star2 = StarDrawer(-50, 0, 'red')

# draw three stars symmetrically
star1.draw_star()
star2.draw_star()
star1.move_to_next(200)
star1.draw_star()

star1.selesai()
star2.selesai()