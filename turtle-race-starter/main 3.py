from turtle import Turtle, Screen
import random
is_race_on = False
all_turtles = []
colors = ["red","orange","pink","black","yellow","green"]
y_positions = [75,45,15,-15,-45,-75]
screen = Screen()
screen.setup(500,400)
user_bet= screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")

# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# tan = Turtle(shape="turtle")
# tee = Turtle(shape="turtle")
# toe = Turtle(shape="turtle")
# top = Turtle(shape="turtle")

# create 6 turtles objects
for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 213:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You win.The winner is {win_color} turtle.")
            else:
                print(f"You lose. The winner is {win_color} turtle.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        # the end loop , when one turtle is end

    
    



# how to do group members
# tim.penup()
# tom.penup()
# tan.penup()
# tee.penup()
# toe.penup()
# top.penup()

# six turtle six colors and at the beginnning line
# tim.color(colors[0])
# tom.color(colors[1])
# tan.color(colors[2])
# tee.color(colors[3])
# toe.color(colors[4])
# top.color(colors[5])
#
# tim.goto(-230, 75)
# tom.goto(-230, 45)
# tan.goto(-230,15)
# tee.goto(-230,-15)
# toe.goto(-230,-45)
# top.goto(-230,-75)



screen.exitonclick()