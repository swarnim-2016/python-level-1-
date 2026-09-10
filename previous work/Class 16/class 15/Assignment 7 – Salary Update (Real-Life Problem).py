list=[12232,3423,342,453,56424546]
for i in range(0,5):
    if list[i]<=2000:
        list[i]=list[i]+200
    else:
        list[i]=list[i]+10/100*list[i]
print(list)                        