n=int(input("n="))
if n<0 or n>9999:
    print("Nhap lại")
else:
    for i in range(1,n+1):
        print(n,"co",len(str(n)),"chu so")
        break
    