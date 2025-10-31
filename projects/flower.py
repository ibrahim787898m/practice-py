from tkinter import mainloop
import turtle

from pip import main
turtle = turtle.Turtle()
turtle.speed(0)

def fleur():
    for i in range(300):
        turtle.circle(190-i, 90)
        turtle.left(90)
        turtle.circle(190-i, 90)
        turtle.left(18)
fleur()
mainloop()

turtle.done()