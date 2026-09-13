contacts=[]
while True:
    print(f"""
1.add contact 
2.remove contact
3.modify contact name
4.display contacts
5.exit""")
    choice =int(input("enter a number"))
    if choice==1:
        contactname=(input("enter a name"))
        contacts.append(contactname)
        print("contact is  submited ")
    elif choice==2:
        recon=(input("enter a number")) 
        contacts.remove(recon)
        print("contact has been removed sucsessfuly")
    elif choice==3:
        ind=int(input("enter a unmber"))
        thename=input("enter real name")
        contacts[ind]=thename
    elif choice==4:
        print(contacts) 
    elif choice==5:
        break
        print("thank you for yousing are app")



