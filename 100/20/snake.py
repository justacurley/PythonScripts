from turtle import Turtle
STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__ (self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)
    def move_snake(self):
        for seg_num in range(len(self.segments)-1,0,-1):
             self.segments[seg_num].goto((self.segments[seg_num-1].xcor()),(self.segments[seg_num-1].ycor()))
        self.head.forward(MOVE_DIST)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def up(self):        
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)        

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)        

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)        
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

