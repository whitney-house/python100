###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.b
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)
turtle.colormode(255)
colors = [(245, 238, 238), (246, 244, 244), (202, 110, 110), (240, 241, 241), (236, 243, 243), (149, 50, 50), (222, 136, 136), (53, 123, 123), (170, 41, 41), (138, 20, 20), (134, 184, 184), (197, 73, 73), (47, 86, 86), (73, 35, 35), (145, 149, 149), (14, 70, 70), (232, 165, 165), (160, 158, 158), (54, 50, 50), (101, 77, 77), (183, 171, 171), (36, 74, 74), (19, 89, 89), (82, 129, 129), (147, 19, 19), (27, 102, 102), (12, 64, 64), (107, 153, 153), (176, 208, 208), (168, 102, 102)]
t = turtle.Turtle()
# this will show no line
t.penup()
t.hideturtle()
# let turtle to the down place
t.setheading(225)
# 7 poinst with 50 paces each one
t.forward(350)
# start from this point to the right
t.setheading(0)
t.speed("fastest")
num_of_line = 10

for _ in range (num_of_line):
    for _ in range (10):
        t.dot(10, random.choice(colors))
        t.forward(50)

    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)








scrren = turtle.Screen()
scrren.exitonclick()