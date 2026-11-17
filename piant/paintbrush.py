import turtle
turtlescreen=turtle.Screen()
arrow=turtle.Turtle("triangle")
def movebackward():
    arrow.backward(10)
def moveleft():
    arrow.left(10)    
def moveright():
    arrow.right(10)
def stopdrawing():
    arrow.penup()
def resumedrawing():
     arrow.pendown()
def colorchanger():
     arrow.pencolor("blue")
def red():
    arrow.pencolor("red")
def movefowrd(): 
    arrow.forward(10)   
size=0
def incresesize():
    global size
    size=size+1
    arrow.pensize(size)
def decresesize():
    global size
    size=size-1
    arrow.pensize(size)
def gotoonclick(x,y):
    arrow.goto(x,y)
def gotonodraw(x,y):
    arrow.penup()
    arrow.goto(x,y)
    arrow.pendown()
def clearscreen ():
    arrow.clear()
def drawsquare():
    for i in range(4):
        arrow.forward(50)
        arrow.left(90)
def drawcircle():
    arrow.circle(10)
def drawstar():
    for i in range(5):
        arrow.forward(i)
        arrow.left(144)
turtlescreen.listen()
turtlescreen.onkey(movefowrd,"a") 
turtlescreen.onkey(movebackward,"s")
turtlescreen.onkey(moveleft,"d")
turtlescreen.onkey(moveright,"f")
turtlescreen.onkey(stopdrawing,"g")
turtlescreen.onkey(resumedrawing,"h")
turtlescreen.onkey(colorchanger,"j")
turtlescreen.onkey(incresesize,"k")
turtlescreen.onkey(decresesize,"l")
turtlescreen.onkey(red,"q")
turtlescreen.onkey(drawsquare,"w")
turtlescreen.onkey(drawcircle,"e")
turtlescreen.onkey(drawstar,"r")
turtlescreen.onkey(clearscreen,"c")
turtlescreen.onscreenclick(gotoonclick,btn=3)
turtlescreen.onscreenclick(gotonodraw,btn=1)



turtle.done()
#"incermenting     
