from turtle import Turtle, Screen
import random

new_turtle = Turtle()


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "blue", "green", "pink", "orange", "violet"]

all_turtles = []

if user_bet or user_bet.lower() in colors:
    is_race_on = True
else:
    print("No bet made. Please make a bet.")
    exit()

for i in range(len(colors)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=-110 + i * 50)
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 240:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The {winner} turtle is the winner!")
            break

screen.exitonclick()