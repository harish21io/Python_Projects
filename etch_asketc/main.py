from turtle import Turtle, Screen

bolt = Turtle()
screen = Screen()

def move_forward():
    bolt.forward(10)

def move_backward():
    bolt.backward(10)

def turn_left():
    bolt.left(10)

def turn_right():
    bolt.right(10)

def clear_screen():
    bolt.clear()
    bolt.penup()
    bolt.home()
    bolt.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()