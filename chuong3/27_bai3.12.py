n=int(input())
s=''
for i in range(1,10):
    a=n%10
    if a==0:
        s='A'+s
    elif a==1:
        s= 'B'+s
    elif a==2:
        s= 'C'+s
    elif a==3 :
        s= 'D'+s
    elif a==4 :
        s= 'E'+s
    elif a==5 :
        s= 'F'+s
    elif a==6 :
        s= 'G'+s
    elif a==7 :
        s= 'H'+s
    elif a==8 :
        s= 'K'+s
    elif a==9 :
        s= 'L'+s
    n=n//10
    if n==0:
        break
    else:
        continue
        
print(s)