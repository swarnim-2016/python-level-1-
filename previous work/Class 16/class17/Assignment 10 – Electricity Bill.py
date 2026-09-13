e=[123,23,23,12,23,12]
for i in range(0,6):
    if e[i]<=1000:
        e[i]=e[i]+100
    else:
        e[i]=e[i]+10/100
print(e[i])    