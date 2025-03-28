from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def counter_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def clear_screan():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear_screan)
screen.exitonclick()