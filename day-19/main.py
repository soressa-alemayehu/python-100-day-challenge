from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)

is_race_on = False

user_bet = screen.textinput(title = "Make your bet", prompt="which turtle will win the race? Enter color: ", )
colors = ["red", "blue", "orange", "yellow", "purple", "green"]
turtle_list = []

n = 0
for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, -100 + n)
    n+= 40
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} Turtle")
            else:
                print(f"You've lost! The {winning_color} Turtle")
        random_move = random.randint(1, 10)
        turtle.forward(random_move)

screen.exitonclick()