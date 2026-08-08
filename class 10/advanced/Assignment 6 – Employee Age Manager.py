ages=[12,23,34,56,23,34,12]
for i in range(0,6):
    if ages[i]>=30:
        if ages[i]%2==0:
            print(ages[i])
            ages[i]=ages[i]+1
for i in range(0,6):
    print(ages)