def groot(name):
    print(f"Hello{name} what can i help you with")
groot("name")

def add (n1,n2):
    return n1+n2
x=add(20,30)
print(x)

def subtract(n1,n2):
    return n1-n2   
y=subtract(23,123)
print(subtract)

def findremander(n1,n2):
    return n1%n2
w=findremander(21,23)
print(w)

def square(n1):
    
    return n1*n1
q=square(2)
print(q)    
    
def cube(n1):
    return n1*n1*n1
r=cube(3)
print(r)

def squareroot(n1):
    return n1**0.5
v=squareroot(24)
print(v)

def f1(n):
    return n*10
x=f1(10)

f = lambda n:n
print(f(10))
       
square=lambda n:n*n
print(square(10))

cube=lambda n:n*n*n
print(cube(3))

squareroot=lambda n:n**0.5
print(squareroot(36))

add=lambda n:n+n
print(add(2))

def cetofa(celcious):
    return celcious*(9/5)+32
print(cetofa(30))

celciousconverson=lambda celcious:celcious*(9/5)+32
print(celciousconverson(23))