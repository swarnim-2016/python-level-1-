#Inputs:
#- age
#- student (yes/no)
#Rules:

#- Base ticket price = ₹200
#- If age < 12 → 50% discount
#- If student → 20% discount
#- Student discount applies **after** age discount
#- Print final amount.
age = int (input("enter your age"))
student = bool (input("enter are you a student by typeing true or false"))

purchaseAmount = float (input("Enter purchase amount : "))
finalAmount = purchaseAmount
discountOnage = 0 
discountOnstudent = 0

if age < 12:
      discountOnage = purchaseAmount * (50/100)
      finalAmount = finalAmount - discountOnage
if student:
    discountOnstudent= purchaseAmount* (20/100) 
    finalAmount=finalAmount- discountOnstudent     
    
        
print(f"""
   -----------Bill Breakout-----------
   Purchase amount        :   {purchaseAmount}
   Discount on age        :   {discountOnage}
   Discount On student     :   {discountOnstudent}
   ------------------------------------
   Final Amount           :   {finalAmount}

""")

























