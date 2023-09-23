p = int(input("Nhập P = "))
al = int(input("Nhập alpha = "))
a = int(input("Nhập a = "))
y = pow(al,a,p)
ps = p-1
print("Khóa công khai Kp = ({},{},{})".format(p,al,y))
print("Khóa bảo mật Ks = ",a)
x = int(input("Bức điện x = "))
k = int(input("giá trị k = "))
print("Khóa ký là ({},{})".format(a,k))
kp = pow(k,-1,ps)
print("Nghịch đảo của k trên vành đai Z(p-1): ",kp)
s1 = pow(al,k,p)
s2 = ((x- a*s1)*kp)%ps
print("Chữ ký trên dữ liệu x = {} là: (S1,S2) = ({},{})".format(x,s1,s2))
ver = pow(pow(y,s1)*pow(s1,s2),1,p)
print("ver(x,s1,s2)= ",ver)
if ver == pow(al,x,p):
	print("Chữ ký là đúng!")
else:
	print("Chữ ký không hợp lệ!")