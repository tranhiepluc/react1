while True:
    n=int(input("n="))
    for i in range(1,n+1):
        if i%2==0:
            print(i,end=" ") 
    print(" ")
    t=input("Tiep tuc khong?")
    if t=="K" or t=="k":
        break