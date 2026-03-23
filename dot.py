import random
import turtle

# setup screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

# setup turtle
tom = turtle.Turtle()
tom.hideturtle()
tom.penup()
tom.speed(0)

# allow RGB colors
turtle.colormode(255)

# colors list
colors = [
    "pink", "red", "orange", "green", "black", "brown",
    "aliceblue", "yellow", "gray", "aquamarine",
    "burlywood", "white"
]

# draw random dots
for _ in range(300):
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    tom.goto(x, y)
    tom.pencolor(random.choice(colors))
    tom.dot(20)

# keep window open
screen.exitonclick()