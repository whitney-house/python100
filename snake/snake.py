from turtle import  Turtle



# constant named in all capital letters
STARTING_POSTIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        # put all segments together
        self.segments = []
        # it will create a snake when call this class
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # for idx in range(3):
        for pos in STARTING_POSTIONS:
            sigment = Turtle("square")
            sigment.color("white")
            sigment.penup()
            # sigment.goto(starting_pos[idx])
            sigment.goto(pos)
            self.segments.append(sigment)

    def add_length(self):
        sigment = Turtle("square")
        sigment.color("white")
        sigment.penup()
        self.segments.append(sigment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_Y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_Y)
        self.segments[0].forward(MOVE_DISTANCE)


    # go up cannot go down, go left cannot go right
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

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]













