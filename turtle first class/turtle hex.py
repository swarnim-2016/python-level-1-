import turtle
screen=turtle.Screen()
screen.bgcolor("yellow")
draw= turtle.Turtle("turtle")
draw.color("green")
draw.color("blue")
draw.speed(0)
draw.pensize(1)
def hexagonigal():
    for i in range(63):
        draw.forward(i)
        draw.left(60)

def spiraltriangle():
    for i in range(300):
        draw.forward(i)        
        draw.left(120)
def square():
    for i in range(234):
        draw.forward(i)
        draw.left(90)

def star():
    for i in range(555):
        draw.forward(i)
        draw.left(144)
       
while True:
    print("""the things you can make are:
     1.hexogon
    2.triangle
     3 square
    4 star   """ )
    choice=int(input("enter the chjoice"))
    if choice==1:
        hexagonigal()
    elif choice==2:
        spiraltriangle()
    elif choice==3:
        square()
    elif choice==4:
        star()            
turtle.done()






   