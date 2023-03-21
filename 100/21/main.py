from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
left_pad = Paddle((-350,0))
right_pad= Paddle((350,0))
ball = Ball()
screen.listen()
screen.onkey(left_pad.up,"w")
screen.onkey(left_pad.down,"s")
screen.onkey(right_pad.up,"Up")
screen.onkey(right_pad.down,"Down")
game_on = True
while game_on:
    time.sleep(0.1)
    ball.move()
    screen.update()
    #detect collision with ceil/floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce()
screen.exitonclick()
