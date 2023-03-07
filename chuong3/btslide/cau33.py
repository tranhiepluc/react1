gia1=550
gia2=750
gia3=950
gia4=1350
tieuthu=int(input("Tieu thu="))
thue=float(input("thue="))
if tieuthu<=100:
    tiendien1=tieuthu*gia1
    print("phai tra=",tiendien1,sep="")
elif tieuthu<=150:
    tiendien2=100*gia1+(tieuthu-100)*gia2
    print("phai tra=",tiendien2,sep="")
elif tieuthu<=200:
    tiendien3=100*gia1+50*gia2+(tieuthu-150)*gia3
    print("phai tra=",tiendien3,sep="")
else: print("phai tra=",tiendien4=100*gia1+50*gia2+50*gia3+(tieuthu-200)*gia4,sep="")

        
        
    