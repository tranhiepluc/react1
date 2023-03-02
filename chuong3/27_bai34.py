toan=int(input("toan:"))
ly  =int(input("ly:"))
hoa =int(input("hoa:"))
dtb=(toan*2+ly*3+hoa)/6
if dtb < 3 :
    print("xep loai kem")
elif 3<=dtb<5 :
    print("xep loai yeu")
elif 5<=dtb<6 :
    print("xep loai trung binh")
elif 6<=dtb<7 :
    print("xep loai trung binh kha")
elif 7<=dtb<8 :
    print("xep loai kha")
elif 8<=dtb<9 :
    print('xep loai gioi')
elif 9<=dtb<10 :
    print("xep loai xuat sac")