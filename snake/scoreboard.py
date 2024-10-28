from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('./data.txt') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,290)
        # write the sore 0
        self.update_scoreboard()

    # delete the previous score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score}  High Score {self.high_score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        # update the score
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('./data.txt',mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)



