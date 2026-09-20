shoppingcart=[]
def additem():
    addingshopping=(input("enter a item"))
    shoppingcart.append(addingshopping)
def removeitem():
    removecart=(input("enter a item to remove")) 
    shoppingcart.remove(removecart)   
def modifyitem():
    realname=input("enter a real name of the item") 
    inxex=int(input("enter a index of the item"))
    shoppingcart[inxex]=realname
def showlist():
    for i in range(len(shoppingcart)):
        print(shoppingcart[i])
while True:
    print("""YOU can do
    1.additem
    2.removeitem
    3.modifyitem
    4.see all items
    5.exit""")
    choice=int(input("enter youer choice "))
    if choice==1:
        additem()
    elif choice==2:
        removeitem()
    elif choice==3:
        modifyitem()
    elif choice==4:
        showlist()
    elif choice==5:
        print("thank you for yousing our application")
        break                               
    else:
        print("the only options are from 1,5 thank you")    