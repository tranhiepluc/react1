m1=int(input('m1='))
m2=int(input('m2='))
m3=int(input('m3='))
tieuthu=int(input('s='))
if tieuthu<=100:
    tien1=tieuthu*m1
    print("Phai tra=",tien1,sep="")
elif tieuthu<=150:
    tien2=m1*100+m2*(tieuthu-100)
    print("Phai tra=",tien2,sep="")
else:
    tien3=m1*100+m2*50+m3*(tieuthu-100-50)
    print("Phai tra=",tien3,sep="")