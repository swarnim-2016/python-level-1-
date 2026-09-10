list[1232,34,234,23,23]
for i in range(0,6):
    if list[i]<=90:
        list[i]=list[i]+10
    elif list[i]<=75 and list[i]<=89:
        list[i]=list[i]+7
    else:
        list[i]=list[i]+5
print(list)                