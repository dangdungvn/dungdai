chuoimh = ""
chuoigm = ""
chuoi = input("Nhập vào chuỗi ban đầu: ")
k = int(input("Nhập k= "))
print("Các ký tự sau khi được mã hóa sẽ trở thành các số: ")
for i in chuoi:
    if i.isalpha():
        if i.isupper():
            somh = (ord(i) - 65 + k) % 26
            ktmh = chr((ord(i) - 65 + k) % 26 + 65)
        else:
            somh = (ord(i) - 97 + k) % 26
            ktmh = chr((ord(i) - 97 + k) % 26 + 97)
    else:
        ktmh = i
    chuoimh += ktmh
    print(" ", somh)
print("Chuỗi sau khi được mã hóa sẽ trở thành: ", chuoimh)
print("Các số sau khi được giải mã:")
for i in chuoimh:
    if i.isalpha():
        if i.isupper():
            sogm = (ord(i) - 65 - k) % 26
            ktgm = chr((ord(i) - 65 - k) % 26 + 65)
        else:
            sogm = (ord(i) - 97 - k) % 26
            ktgm = chr((ord(i) - 97 - k) % 26 + 97)
    else:
        ktgm = i
    chuoigm += ktgm
    print(" ", sogm)
print("Chuỗi sau khi được giải mã: ", chuoigm)
