a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max=a
if max<b and b>c:
    max=b
elif max<c and c>b:
    max=c
print("SLN=",max,sep="")
min=a
if min>b and b<c:
    min=b
elif min>c and c<a:
    min=c
print("SBN=",min,sep="")