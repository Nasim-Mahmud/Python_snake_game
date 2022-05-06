from turtle import Turtle, Screen

turtle_pos = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.ggturtles = []
        self.create_snake()
        self.head = self.ggturtles[0]

    def create_snake(self):
        for pos in turtle_pos:
            self.add_turtle(pos)

    def add_turtle(self, pos):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.ggturtles.append(tim)

    def extend(self):
        self.add_turtle(self.ggturtles[-1].position())

    def move(self):
        for n in range(len(self.ggturtles) - 1, 0, -1):
            x_pos = self.ggturtles[n - 1].xcor()
            y_pos = self.ggturtles[n - 1].ycor()
            self.ggturtles[n].goto(x_pos, y_pos)
        self.head.forward(MOVE)

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

    def reset_snake(self):
        self.ggturtles.clear()
        self.create_snake()
