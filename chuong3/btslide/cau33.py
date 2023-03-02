giadienmuc1=int(input("m1="))
giadienmuc2=int(input("m2="))
giadienmuc3=int(input("m3="))
sokwtieuthu=int(input("Tieu thu="))
thue=float(input("thue="))
if sokwtieuthu>100:
    a=sokwtieuthu-100
    x=sokwtieuthu-a
    tien1=x*giadienmuc1
    if a>50:
        b=a-50
        c=a-b
        tien2=c*giadienmuc2
        tien3=b*giadienmuc3
        print("Phai tra=",(tien1+tien2+tien3)+(tien1+tien2+tien3)*thue)
    elif a<50:
        tien2=a*giadienmuc2
        print("phai tra=",(tien2+tien1)+(tien2+tien1)*thue)
else:
    print("phai tra=",tien1,sep="")
        
    