from turtle import Turtle

# in this case the paddle can inheritate from Turtle class
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__() # to inherite from Turtle
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position) # this parameter is good for different paddlers' position setting

    def go_up(self):
        self.goto(self.xcor(),self.ycor()+20)

    def go_down(self):
        self.goto(self.xcor(),self.ycor()-20)

