n=int(input("Nhập vào số nguyên n (2<=n<=50)"))
i=2
while n>2 or n<50:
    if n%2==0:
        print(i,end=" ")
    i=i+2