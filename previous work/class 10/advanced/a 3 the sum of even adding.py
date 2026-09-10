no=[11,22,33,44,55]
for i in range(0,4):
    if no[i]%2==0:
        no[i]= no[i]*10
    else:
        no[i]=no[i]+5
print(no)            