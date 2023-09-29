import numpy as np
import math
import sys


def inmatran(k):
	for r in k:
		for j in r:
			print(j, end=' ')
		print()


k = []
ks = []
s = input("Nhập S:")
c = ""
d = ""
ds = ""
dd = ""
t =""
s = s.upper()

if len(s) % 3 == 1:
	s += "AA"
	idx = 1
elif len(s) % 3 == 2:
	s += "A"
	idx = 2
else:
	idx = 0
print(s)
print("Nhập các phần tử của ma trận k: ")
for i in range(3):
	r = []
	for j in range(3):
		pt = int(input("Nhập phần tử [{},{}]: ".format(i, j)))
		r.append(pt)
	k.append(r)
inmatran(k)
kn = np.array(k)
dk = np.linalg.det(kn)
dk = int(dk)
print("det(K)= ", dk)
print("GCD của det(k) và Z là: ", math.gcd(dk, 26))

for i in range(0, len(s), 3):
	if s[i].isalpha():
		so1 = ((ord(s[i]) - 65) * k[0][0] + (ord(s[i+1]) - 65) * k[1][0] + (ord(s[i+2]) - 65) * k[2][0])
		so2 = ((ord(s[i]) - 65) * k[0][1] + (ord(s[i+1]) - 65) * k[1][1] + (ord(s[i+2]) - 65) * k[2][1])
		so3 = ((ord(s[i]) - 65) * k[0][2] + (ord(s[i+1]) - 65) * k[1][2] + (ord(s[i+2]) - 65) * k[2][2])
		d = " " + str(so1) + " " + str(so2) + " " + str(so3)
	ds += d
print("Chuỗi số sau khi nhân: ", ds)
for i in range(0, len(s), 3):
	if s[i].isalpha():
		so4 = (((ord(s[i]) - 65) * k[0][0] + (ord(s[i+1]) - 65) * k[1][0] + (ord(s[i+2]) - 65) * k[2][0]) % 26)
		so5 = (((ord(s[i]) - 65) * k[0][1] + (ord(s[i+1]) - 65) * k[1][1] + (ord(s[i+2]) - 65) * k[2][1]) % 26)
		so6 = (((ord(s[i]) - 65) * k[0][2] + (ord(s[i+1]) - 65) * k[1][2] + (ord(s[i+2]) - 65) * k[2][2]) % 26)
		d = " " + str(so4) + " " + str(so5) + " " + str(so6)
	dd += d
print("Chuỗi số sau khi mod Z: ", dd)
for i in range(0, len(s), 3):
	if s[i].isalpha():
		ktmh1 = chr((((ord(s[i]) - 65) * k[0][0] + (ord(s[i+1]) - 65) * k[1][0] + (ord(s[i+2]) - 65) * k[2][0]) % 26) + 65)
		ktmh2 = chr((((ord(s[i]) - 65) * k[0][1] + (ord(s[i+1]) - 65) * k[1][1] + (ord(s[i+2]) - 65) * k[2][1]) % 26) + 65)
		ktmh3 = chr((((ord(s[i]) - 65) * k[0][2] + (ord(s[i+1]) - 65) * k[1][2] + (ord(s[i+2]) - 65) * k[2][2]) % 26) + 65)
		t = ktmh1 + ktmh2 + ktmh3
	c += t
print("Chuỗi sau khi mã hóa: ", c)
if idx == 1:
	c = c[:len(c)-2]
if idx == 2:
	c = c[:len(c)-1]
print("Chuỗi sau khi cắt các phần tử thừa: ", c)
