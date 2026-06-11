#Write a “Shopping Combo Checker”:

#3Input:

#- hasCoupon (yes/no)
#- isFestival (yes/no)
#- price

#If (hasCoupon or isFestival) and price > 800 → give 12% discount.

#Else → no discount.
coupon= bool(input("enter do you have a coupon "))
festival=bool (input("is it a festival "))
price=100
final = price
if  coupon==True and price >800:
    price-(12/100)    
if festival==True and price>800:
    price - (12/100) 
print (final)        










