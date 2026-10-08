import turtle
import random
shapes=["hexogon","triangle","star","square"]
comchoice=random.choice()
guess=input("enter the chioce that you think the computer will choice to unlokk the picture")    
seren = turtle.Screen
pointer = turtle.Turtle("square")
pointer.speed(0)
def star():
    for i in range(100):
        pointer.goto(x=150,y=150)x = random .randit(150,150)
        pointer.forward(i)
        pointer.left(144)

def tringle():
    for i in range(100):
            pointer.forward(i)
            pointer.left(120)
            pointer.goto(x=200,y=50),y=random.randint(200,50)
def square():    
    pointer.goto(x=200,y=50),y=random.randint(200,50)
    for i in range(100):
        pointer.forward(i)
        pointer.left(90)    
#60 90
def hexogon():
    for i in range(2342):
         pointer.forward(60)
         pointer.forward(90)
if comchoice==guess:
     print("you won")
if comchoice==hexogon:
     hexogon()
elif comchoice==tringle:
     tringle()
elif comchoice==square:
     square()
elif comchoice==star:
     star()
else:
     print("you lost")
     







turtle.done()