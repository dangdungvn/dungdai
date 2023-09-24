import math
import sys
chuoimh = ""
chuoigm = ""
chuoi = input("Nhập chuỗi ban đầu: ")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
t = math.gcd(a, 26)
if t == 1:
    d = pow(a, -1, 26)
    print(d)
else:
    print("Phần tử a không có nghịch đảo trên n")
    sys.exit()
print("Các ký tự sau khi được mã hóa sẽ trở thành các số:")
for i in chuoi:
    if i.isalpha():
        if i.isupper():
            somh = (a*(ord(i)-65)+b) % 26
            ktmh = chr((a*(ord(i)-65)+b) % 26 + 65)
        else:
            somh = (a*(ord(i)-97)+b) % 26
            ktmh = chr((a*(ord(i)-97)+b) % 26 + 97)
    else:
        ktmh = i
    chuoimh += ktmh
    print(" ", somh)
print("Chuỗi sau khi được mã hóa sẽ trở thành: ", chuoimh)
print("Các số sau khi được giải mã:")
for i in chuoimh:
    if i.isalpha():
        if i.isupper():
            sogm = (d*(ord(i) - 65 - b)) % 26
            ktgm = chr((d*(ord(i) - 65 - b)) % 26 + 65)
        else:
            sogm = (d*(ord(i) - 97 - b)) % 26
            ktgm = chr((d*(ord(i) - 97 - b)) % 26 + 97)
    else:
        ktgm = i
    chuoigm += ktgm
    print(" ", sogm)
print("Chuỗi sau khi được giải mã: ", chuoigm)
