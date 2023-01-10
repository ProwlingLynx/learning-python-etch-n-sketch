from turtle import Turtle, Screen
from random import randint

screen = Screen()
joe = Turtle()
tim = Turtle()
sam = Turtle()
judy = Turtle()

joe.color("purple")
tim.color("green")
sam.color("blue")
judy.color("black")

turtle_list = [joe, sam, judy]


def move_forward(turtle):
    turtle.forward(10)


def move_backward(turtle):
    turtle.back(10)


def turn_left(turtle):
    turtle.left(10)
    move_forward(turtle)


def turn_right(turtle):
    turtle.right(10)
    move_forward(turtle)


def clear_board(turtle):
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


turtle_move = [move_forward, move_backward, turn_left, turn_right]


def random_move(turtle):
    random_index = randint(0, 3)
    random_turtle_move = turtle_move[random_index]
    random_turtle_move(turtle)


def game_forward():
    move_forward(tim)
    for turtle in turtle_list:
        random_move(turtle)


def game_backward():
    move_backward(tim)
    for turtle in turtle_list:
        random_move(turtle)


def game_right():
    turn_right(tim)
    for turtle in turtle_list:
        random_move(turtle)


def game_left():
    turn_left(tim)
    for turtle in turtle_list:
        random_move(turtle)


def game_clear():
    clear_board(tim)
    for turtle in turtle_list:
        clear_board(turtle)


screen.listen()

screen.onkey(fun=game_forward, key="w")
screen.onkey(fun=game_backward, key="s")
screen.onkey(fun=game_left, key="a")
screen.onkey(fun=game_right, key="d")
screen.onkey(fun=game_clear, key="space")

screen.exitonclick()
