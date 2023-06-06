from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Paddle(Turtle):
    def __init__ (self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.pu()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(),(self.ycor() + 20))
    def down(self):
        self.goto(self.xcor(),(self.ycor() - 20))
