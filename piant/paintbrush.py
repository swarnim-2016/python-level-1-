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
    arrow.pencolor("red")
def movefowrd(): 
    arrow.forward(10)   
turtlescreen.listen()
turtlescreen.onkey(movefowrd,"a") 
turtlescreen.onkey(movebackward,"s")
turtlescreen.onkey(moveleft,"d")
turtlescreen.onkey(moveright,"f")
turtlescreen.onkey(stopdrawing,"g")
turtlescreen.onkey(resumedrawing,"h")
turtlescreen.onkey(colorchanger,"j")




turtle.done()