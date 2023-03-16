while True:
    a=float(input("a="))
    b=float(input("b="))
    n=input("toan tu:")
    if n=="+":
        print(str(a),"+",str(b),"=",a+b,sep="")
    elif n=="-":
        print(str(a),"-",str(b),"=",a-b,sep="")
    elif n=="*":
        print(str(a),"*",str(b),"=",a*b,sep="")
    elif n=="/":
        if b!=0:
            print(str(a),"/",str(b),"=",a/b,sep="")
    k=input("Tiep tuc:")
    if k=="t" or k=="T":
        break
    
       
        
    
    
    
    