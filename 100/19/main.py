from turtle import Turtle, Screen
import random
colors = ["red","green","blue","yellow","black"]
#tim = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    out = (r,g,b)
    return out
# screen.listen()
# forwards
#def move_forwards():
#    tim.forward(10)
#screen.onkey(key="w",fun=move_forwards)
#def move_backwards():
#    tim.backward(10)
#screen.onkey(key="s",fun=move_backwards)
#def move_left():
#    tim.left(10)
#screen.onkey(key="a",fun=move_left)
#def move_right():
#    tim.right(10)
#screen.onkey(key="d",fun=move_right)
#def clean_screen():
#    tim.clear()
#    tim.penup()
#    tim.home()
#    tim.pendown()
#screen.onkey(key="c",fun=clean_screen)

bet = screen.textinput("Choose Turtle","Who will win the race?")
turtles = [Turtle() for i in range(len(colors))]
for i in range(len(turtles)):
    turtle=turtles[i]
    turtle.color(colors[i])
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x=-230,y=-100+(i*50))
racing = True
while racing:
    for i in range(len(turtles)):
        turtle=turtles[i]
        turtle.forward(random.randrange(10, 100, 10))
        if turtle.position()[0] >= 210:
            racing=False
            winner = turtle.color()[0]
print("The winning turtle was {}".format(winner))
screen.exitonclick()
