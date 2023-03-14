from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(10)
tim.speed(10)
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
colors = ["red","green","blue","yellow","cyan","orange","pink","black","grey"]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    out = (r,g,b)
    return out
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
# for i in range(3,11):
#     draw_shape(i)
directions = [0,90,180,270]
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
