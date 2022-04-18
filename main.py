from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
# TODO: there are various methods to make snakes
# x = 0
# for n in range(0, 3):
#     tim = Turtle("square")
#     tim.penup()
#     tim.color("white")
#     tim.setx(x)
#     x += 20

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
ggturtles = []

for position in starting_pos:
    new_turtle = Turtle("square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(position)
    ggturtles.append(new_turtle)

# screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    for tur_num in range(len(ggturtles) - 1, 0, -1):
        new_x = ggturtles[tur_num - 1].xcor()
        new_y = ggturtles[tur_num - 1].ycor()
        ggturtles[tur_num].goto(new_x, new_y)
    ggturtles[0].forward(20)
    ggturtles[0].left(90)

screen.exitonclick()
