from turtle import Screen, Turtle


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black ")
screen.title("my snake game")

starting_positions = [(0,0), (-20,0), (-40,0)]

for position in starting_positions:
    snake = Turtle("square")
    snake.color("white")
    snake.goto(position)








screen.exitonclick()