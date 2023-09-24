import math
import sys
p = int(input("Nhập p: "))
q = int(input("Nhập q: "))
e = int(input("Nhập e: "))
n = p*q
print("N = ", n)
dn = (p-1) * (q-1)
print("phi N = ", dn)
if e >= dn or e <= 1:
    print("Hệ lỗi!")
    sys.exit()
d = pow(e, -1, dn)
print("d = ", d)
print("Khóa công khai Kp: (e,n) = ({},{})".format(e, n))
print("Khóa bảo mật Ks: (d,n) = ({},{})".format(d, n))
while True:
    temp = int(input("""
Nhập 1: mã hóa thông điệp
Nhập 2: giải mã thông điệp
Nhập 3: tạo chữ ký số
Nhập 4: kết thúc chương trình
Số tương ứng: """))
    if temp == 1:
        m = int(input("Nhập vào bản rõ : M = "))
        c = pow(m, e, n)
        print("Bản mã thu được: C = ", c)
    elif temp == 2:
        c = int(input("Nhập vào bản rõ : C = "))
        m = pow(c, d, n)
        print("Bản mã thu được: M = ", m)
    elif temp == 3:
        m = int(input("Nhập vào bản mã của chữ ký: M = "))
        s = pow(m, d, n)
        print("Chữ ký là: ", s)
        print("Kiểm tra chữ ký số!")
        md = pow(s, e, n)
        if m == md:
            print("Chữ ký hợp lệ!")
    else:
        print("Chương trình kết thúc!")
        sys.exit()
