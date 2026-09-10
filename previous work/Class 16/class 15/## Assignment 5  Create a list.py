list=[1,2,3,2342,232,23]
for i in range(0,6):
    if i%3==0:
        list[i]=list[i]*5
    else:
        list[i]=list[i]+2
print(list)        