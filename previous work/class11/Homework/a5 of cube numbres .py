no1 = int(input("enter a number"))
no2 = int(input("enter a number"))
for i in range(no1,no2):
    if i%2==0 and i%5==0:
        print(i*i*i)