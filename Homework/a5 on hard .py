
#- food total
#- service charge % (5 or 10)
#- membership (yes/no)

#Rules:

#- Add service charge
#- If membership yes → 5% discount on final bill
#- Print detailed bill using f-string.
food= float (input("enter total food cost"))
service = int(input("enter your service percentage 5per or10 per"))
member=bool (input("enter true or false"))
memberdis= 0
total = (food - memberdis)+ service
if member == True:
    memberdis=(5/100)*food
if service==5:
    service=(5/100)*(food-member)
if service==10:
    service=(10/100)*(food- member)
print(f"""----------------bill------------------
                    food:{food}
                 service:{service}
                memberdis:{memberdis}
                total: {total}    

""")


