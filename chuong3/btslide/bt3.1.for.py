while True:
    n=int(input("n="))
    for i in range(1,n+1):
        if n<1 or n>50:
            print("nhap sai,yeu cau nhap lai")
            n=int(input("n="))
    break