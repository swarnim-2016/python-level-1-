books = []
while True:
    print(""" can do:
    1.add book
    2.remove book
    3.modify book
    4.print all books
    5.end""")
    choice=int(input("enter a number :"))
    if choice==1:
        bookadd=(input("enter a book :"))
        books.append(bookadd)
    elif choice==2:
        rebook=input("enter a book :")
        books.remove(rebook)
    elif choice ==3:
        mb = input("enter a real book name: ") 
        thein=int(input("enter a number: "))
        books[thein]==mb
    elif choice==4:
        print(books)
    elif choice==5:
        break
        print("thank")    
