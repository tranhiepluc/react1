n=int(input("Nhập từ bàn phím số nguyên n (n>=1):"))
for i in range(1,n+1):
    if i%5!=0:
        print(i,end=" ")
    if i%5==0:
        print(i)
    