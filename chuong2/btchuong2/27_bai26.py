hoten   = input("ho ten:")
giangaycong = int(input("don gia ngay cong:"))   
songaycong = int(input("so ngay cong:"))       
sophucap = float(input("so phu cap:"))        
tamung = int(input("tien tam ung:"))        
luong = giangaycong*songaycong*sophucap                                 
thuclinh = luong - tamung                             
print("Nhan vien",hoten,", Co tien luong=",round(luong,1),", Tam ung=",tamung," va Thuc linh=",round(thuclinh,1),sep="")
