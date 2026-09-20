def showname():
    print("swarnim")
def showwelcome():
    print("hello" )
def showcourse():
    print("rice")
while True:
    print("""menu
            1.showname
            2.welcome
            3 . the course
            4 . exit""")
    choice=int(input("enter a unmber"))
    if choice==1:
        showname()            
    elif choice==2:
        showwelcome()
    elif choice==3:
        showcourse()
    elif choice==4:
        print("thank you ")
        break        