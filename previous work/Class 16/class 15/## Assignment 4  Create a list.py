#     0 1   2   3   4  
list=[1,23,34,656,67]
for i in range(0,5):
    if list[i]>=15:
        list[i]=list[i]-5
    else:
        list[i]=list[i]+10
print(list)    