from turtle import Turtle, Screen
from random import choice



colors = ['red', 'blue', 'green', 'brown', 'orange' ]
tim = Turtle()

n = 3
while n < 11:
    for _ in range(n):
        tim.right(360/n)
        tim.forward(90)
    tim.color(choice(colors))
    n += 1


screen = Screen()
screen.exitonclick()