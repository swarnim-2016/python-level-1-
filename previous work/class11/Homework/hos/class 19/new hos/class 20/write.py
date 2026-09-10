# #def groot()
#  #   print(hello)
# #groot()
# #def greet():
#  #   print("bye bye")
# #greet()    
# def coffiein():
#     print("pour milk")
#     print("mix")
#     print("pour in cup")
# coffiein()
# coffiein()
# def teamaker():
#    print("make tea")
#    print("pour into cup")
# teamaker()
# teamaker()   
def add():
    no1 = int(input("entera number"))
    no2 = int (input("enter a number"))
    sun=no1+no2
    print(f"the ans of{no1}+{no2}={sun}")
def subtr():
    no3=int(input("enter a number"))
    no4=int(input("enter a number"))
    differ=no3-no4
    print(f"{no3}-{no4}={differ}")
def mul():
    no1=int(input("enter a number"))
    no2 = int(input("enter a number"))
    pro=no1*no2
    print(f"{no1}*{no2}={pro}")
def div():
    no1 = int(input("enter a number"))
    no2 = int(input("enter a number"))
    q=no1/no2
    print(f"{no1}/{no2}={q}")
while True:
    print(""" 
    1 addition 
    2 subtration
    3 multiplication
    4 divition
""")
    choice=int(input("enter a choice"))    
    if choice==1:
        add()    
    elif choice==2:
        subtr()
    elif choice==3:
        mul()
    elif choice ==4:
        div()
        

