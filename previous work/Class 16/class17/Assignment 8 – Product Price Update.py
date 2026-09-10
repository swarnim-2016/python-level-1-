price=[12323,43482374239482,445353,453521445,4545353,231,32,342,34]
for i in range(0,9):
    if price[i]<=500:
        price[i]=price[i]+50
    else:
        price[i]=price[i]+10/100 
print(price)           
