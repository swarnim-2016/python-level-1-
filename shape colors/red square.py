import turtle
screen=turtle.Screen()
screen.bgcolor("blue")
make=turtle.Turtle("turtle")
make.speed(0)
make.color("red")
make.fillcolor("red")
make.begin_fill()

for i in range(100):
    make.forward(50)
    make.left(90)
make.end_fill()    


turtle.done()