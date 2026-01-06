import colorgram
from random import choice
from turtle import Turtle, Screen

bolt = Turtle()
bolt.shape("turtle")
#bolt.speed(0)

screen = Screen()
screen.colormode(255)

colors = colorgram.extract("hirst.jpg",10)
pic_color = []

def color_palette():
    for i in range(len(colors)):
        ex_color = colors[i]
        rgb = ex_color.rgb
        pic_color.append((rgb.r,rgb.g,rgb.b))
    return pic_color

def hirst_art(rows, dots_per_row):
    # Set the starting position (bottom left) so the art is centered
    bolt.penup()
    bolt.setheading(225)
    bolt.forward(300)
    bolt.setheading(0)
    for row_count in range(rows):
        for _ in range(dots_per_row):
            bolt.dot(20, choice(color_palette()))
            bolt.penup()
            bolt.forward(50)
            bolt.pendown()
        # Move to the start of the next row
        bolt.penup()
        bolt.backward(50 * dots_per_row)  # Go back to the start of the line
        bolt.left(90)
        bolt.forward(50)  # Move up to the next row
        bolt.right(90)
        bolt.pendown()

hirst_art(5,5)

screen.exitonclick()