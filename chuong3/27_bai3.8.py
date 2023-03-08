h=6
n=int(input("Nhập vào một số nguyên n (1<=n<=20):"))
k=input("Nhập vào một ký tự bất kỳ:")
for i in range(1,h+1):
    if i<=1:
        print(k*i)
        if i*k=="*":
            print(n)
            if i==1:
                print(i*k)
    else:
        print(i*k)
