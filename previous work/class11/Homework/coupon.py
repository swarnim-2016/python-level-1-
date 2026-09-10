purchaseAmount = float (input("Enter purchase amount : "))
couponCode = input("Enter coupon: ")
finalAmount = purchaseAmount
# variables
validCoupon = "SAVE10"
discountOn500 = 0 #initially consider that as 0
discountOnCoupon = 0

if purchaseAmount > 500:
      discountOn500 = purchaseAmount * (5/100)
      finalAmount = finalAmount - discountOn500
if couponCode == validCoupon:
      discountOnCoupon = 50
      finalAmount = finalAmount - discountOnCoupon
      
print(f"""
   -----------Bill Breakout-----------
   Purchase amount        :   {purchaseAmount}
   Discount On 500        :   {discountOn500}
   Discount On Coupon     :   {discountOnCoupon}
   ------------------------------------
   Final Amount           :   {finalAmount}

""")