a=float(input("a="))
b=float(input("b="))
n=input("Phep toan:")
i=1
while i<=a or i<=b:
    if n=="+":
        print(str(a),"+",str(b),"=",a+b,sep="")
    elif n!="t" or n!="T":
        print("tiep tuc:",n,sep="")
    elif n=="-":
        print(str(a),"-",str(b),"=",a-b,sep="")
    elif n=="*":
        print(str(a),"*",str(b),"=",a*b,sep="")
    elif n=="/":
        print(str(a),"/",str(b),"=",a/b,sep="")
    i=i+1
    continue
    
    
    
    