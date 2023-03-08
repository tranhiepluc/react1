n=int(input("n="))
if n<2 or n>100:
    print("nhap lai")
else:
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,"Khong la SNT")
            break
    else:
        print(n,"la SNT")
    