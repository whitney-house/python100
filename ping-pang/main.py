from turtle import Screen
from paddle import Paddle
from ball import Ball
import time  # slow down the move
from scoreboard import Scoreboard


# initialize the screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0) # show no movement

# initialize two paddlers
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()
# listen to keyboard
screen.listen()

# call methods of go up and go down
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down") # call function as paraeter, no need to pass ()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_spped)
    screen.update() # to show the turtles
    ball.move()

    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.x_move >340:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.x_move > -340:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()









screen.exitonclick()

