x= float(input("x="))
y= float(input("y="))
ch=input("phep toan:")
if ch == "+" :
    print(x,ch,y,"=",round(x+y,1),sep="")
elif ch == "-":
    print(x,ch,y,"=",round(x-y,1),sep="")
elif ch == "*":
    print(x,ch,y,"=",round(x*y,1),sep="")
elif ch == "/":
    if y==0:
        print("khong hop le")
    else:
        print(x,ch,y,"=",round(x/y,1),sep="")
else:
    print('khong hop le')