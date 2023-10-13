import sys
p = int(input("Nhập P = "))
a = int(input("Nhập a = "))
x = int(input("Nhập x = "))
y = pow(a, x, p)
print("y = ", y)
print("Khóa công khai Kp:({},{},{})".format(p, a, y))
print("Khóa bảo mật Ks:({})".format(x))
while True:
    temp = int(input("""
Nhập 1: mã hóa thông điệp
Nhập 2: giải mã thông điệp
Nhập 3: kết thúc chương trình
Số tương ứng: """))
    if temp == 1:
        m = int(input("Nhập bản rõ M = "))
        k = int(input("Chọn k = "))
        khoa = pow(y, k, p)
        print("khóa của hệ: K = ", khoa)
        c1 = pow(a, k, p)
        c2 = (khoa * m) % p
        print("Bản mã được gửi đi là: C = ({},{})".format(c1, c2))
    elif temp == 2:
        c1 = int(input("Nhập bản mã C1 = "))
        c2 = int(input("Nhập bản mã C2 = "))
        khoa = pow(c1, (p-1-x), p)
        print("Khóa của hệ: K = ", khoa)
        m = (khoa*c2) % p 
        print("Bản rõ M = {}".format(m))
    else:
        print("Kết thúc chương trình!")
        sys.exit()
