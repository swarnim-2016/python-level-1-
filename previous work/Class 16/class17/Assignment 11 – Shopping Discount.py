list=[12,34231,342,434,23]
for i in range (0,5):
    if list[i]>=1000:
        list[i]=list[i]-20/100
    else:
        list[i]=list[i]-10/100  
print(list)          