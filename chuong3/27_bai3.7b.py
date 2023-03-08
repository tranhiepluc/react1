n=int(input("n="))
if n>0 :
    print("nhap lai")
else:     
    giaithua=1
    for i in range(1,n+1):
        giaithua=giaithua*i
    print(n,"!=",giaithua,sep="")