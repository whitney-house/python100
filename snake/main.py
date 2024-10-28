from turtle import Screen
import time
from  snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.title("Weiting's Game")
screen.screensize(600,600)
# to avoid the weird uncontinuation of segments
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()


# keyboard
screen.listen()

# call function , remove ()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    # show the seg in a wholem not piece by piece
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collison of food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_length()
        scoreboard.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() <= -295  \
        or snake.head.ycor() > 295 or snake.head.ycor() <= -295:
        #game_is_on = False
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # detect collision with tail

    for seg in snake.segments[1:]: # so no need to write if sanke,head.distance(head)
        if snake.head.distance(seg) < 10:
            #game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
























screen.exitonclick()