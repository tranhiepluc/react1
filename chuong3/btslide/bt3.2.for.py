n=int(input("n="))
for i in range(1,n+1):
    if i %10!=0:
        print(i,end=" ")
    if i %10==0:
        print(i)
