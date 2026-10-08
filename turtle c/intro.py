import turtle
import random

serren = turtle.Screen()
serren.bgcolor("#f50905")
pen=turtle.Turtle("turtle")
pen.color("green")
pen.color("yellow")
pen.pensize(1)
cololist=["yellow","blue","orange"]
pen.speed(0)
for i in range(4):
    pen.pencolor(random. choice(cololist))
    pen.forward(90)
    pen.left(60)        
turtle.done()