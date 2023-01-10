from turtle import *

color("green")

def move_forward():
    forward(10)

def move_backward():
    back(10)

def turn_left():
    left(10)

def turn_right():
    right(10)

listen()

onkey(fun=move_forward, key="w")
onkey(fun=move_backward, key="s")
onkey(fun=turn_left, key="a")
onkey(fun=turn_right, key="d")

exitonclick()