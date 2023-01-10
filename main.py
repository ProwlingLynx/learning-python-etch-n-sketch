from turtle import Turtle, Screen

joe = Turtle()
screen = Screen()

joe.color("green")


def move_forward():
    joe.forward(10)


def move_backward():
    joe.back(10)


def turn_left():
    joe.left(10)


def turn_right():
    joe.right(10)


def clear_board():
    joe.clear()
    joe.penup()
    joe.home()
    joe.pendown()


screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_board, key="space")

screen.exitonclick()