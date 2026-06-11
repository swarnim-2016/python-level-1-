name =(input("enter your name"))
math = int(input("enter your score for math"))
bio = int(input("enter your bio grade"))
en = int(input("enter your marks for engenering"))
total=math+bio+en
per=total/3
res=""
if per>90 and per>100:
    res ="grade A"
elif per>80 and per<90:
    res="grade b"
elif per>70 and per <80:    
    res="grade c"
else:
    res="you faled try again"
print(f"""---------------your grade-------------------------                     name{name}                                                  math={math}                                                 bio={bio}                                                   en={en} 
                    total{total}        

en:{en }
bio{bio}
res{res}
""")

