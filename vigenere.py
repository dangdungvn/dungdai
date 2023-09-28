# Nhập vào bản rõ
import sys
# lựa chọn
while True:
	d = int(input("""
Nhập 1: mã hóa thông điệp
Nhập 2: giải mã thông điệp
Nhập 3: tím khóa k
Nhập 4: kết thúc chương trình
Số tương ứng: """))
	if d == 1:
		# mã hóa bản rõ
		chuoi = input("Nhập vào bản rõ: ")
		chuoimh = ""
		chuoigm = ""
		khoa = input("Nhập vào key: ")
		m = len(khoa)
		chuoi = chuoi.replace(" ", "")
		for i in range(len(chuoi)):
			ktmh = chuoi[i]
			k = khoa[i % m]
			if chuoi[i] == ' ':
				ktmh = ' '
			else:
				if ktmh.isalpha():
					if ktmh.isupper():
						chu = ord('A')
					else:
						chu = ord('a')
					ktmh = chr((ord(ktmh) - chu + ord(k) - chu) % 26 + chu)
			chuoimh += ktmh
		print("Bản mã khi đã được mã hóa: ", chuoimh)
	# giải mã bản mã
	elif d == 2:
		chuoimh = input("Nhập vào bản mã: ")
		chuoigm = ""
		khoa = input("Nhập vào key: ")
		m = len(khoa)
		for i in range(len(chuoimh)):
			ktgm = chuoimh[i]
			k = khoa[i % m]
			if chuoimh[i] == ' ':
				ktgm = ' '
			else:
				if ktgm.isalpha():
					if ktgm.isupper():
						chu = ord('A')
					else:
						chu = ord('a')
					ktgm = chr((ord(ktgm) - chu - ord(k) + chu) % 26 + chu)
			chuoigm += ktgm
		print("Bản rõ sau khi được giải mã: ", chuoigm)
	# Tìm khóa
	elif d == 3:
		chuoi = input("Nhập vào bản rõ: ")
		m = int(input("Độ dài của key: "))
		khoa = ""
		chuoimh = input("Nhập vào bản mã: ")
		chuoisua = chuoi.replace(" ", "")
		for i in range(len(chuoisua)):
			ktmh = chuoisua[i]
			ktgm = chuoimh[i]
			if ktgm.isalpha():
				if ktgm.isupper():
					chu = ord('A')
				else:
					chu = ord('a')
			ktkey = chr((ord(ktgm) - ord(ktmh)) % 26 + chu)
			khoa += ktkey
		khoa = khoa[:m]
		print("Key của chuỗi là: ", khoa)
	else:
		sys.exit()
