
import math
import turtle
 
win = turtle.Screen()
win.bgcolor("white")


# coordinate setting
win.setworldcoordinates(0, -10, 3600, 10)
t = turtle.Turtle()

t.speed(0)

# Generate wave form

for x in range(3600):
    y = math.sin(math.radians(x))
    t.goto(x, y)