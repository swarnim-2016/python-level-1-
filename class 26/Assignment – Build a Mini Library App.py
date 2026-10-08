
books=[]
def addbook():
    book=(input("enter a book"))
    books.append(book)
    print("the book is in the list")
def removebook():
    rebook=input("enter the book you want to remove from the list:")
    books.remove(rebook)
    print("the book was removed")
def modify():
    name = input("enter the name of the book you want to change:")
    index= books.index(name)

    real= input("enter the new name that you want :" )
    books[index]=real 
def display():
    for i in range(len(books) ):
        print(books[i])
while True:
    print("""You Can Do
    1.add book
    2 remove book
    3 modify book
    4 display all books
    5 exit """)
    choice = int(input("enter a number:"))
    if choice==1:
        addbook()
    elif choice==2:
        removebook()
    elif choice==3:
        modify()
    elif choice==4:
        display()
    elif choice==5:
        print("thank you")
        break                        
    else:
        print("there is an invalid option")    
        