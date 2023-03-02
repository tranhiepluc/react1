m1=int(input('m1='))
m2=int(input('m2='))
m3=int(input('m3='))
s=int(input('nhap so dien tieu thu: '))
if s>=100:
    a=s-100
    x=s-a
    gia1=m1*x
    if a>50:
        b=a-50
        y=a-b
        gia2=m2*y
        gia3=b*m3
        print('so tien tra:',gia1+gia2+gia3)
    elif a<=50: 
        gia2=m2*a
        print('so tien tra:',gia1+gia2)
else: 
    print('so tien phai tra:',s*m1)
