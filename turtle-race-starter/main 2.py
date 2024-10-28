from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()
def forwards():
    tim.forward(60)

def backwards():
    tim.backward(60)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# w = forwards
screen.onkey(forwards, "w")
# S for backwards
screen.onkey(backwards, "s")
#A for counter-clockwise 逆时针
screen.onkey(turn_left, "a")
#D for clockwise
screen.onkey(turn_right,"d")
# C for clear
screen.onkey(clear, "c")



screen.exitonclick()