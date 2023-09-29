import math
import sys
import numpy as np


def kadd(matrix, mod):
	rows = len(matrix)
	cols = len(matrix[0])
	result = [[0 for _ in range(cols)] for _ in range(rows)]

	for i in range(rows):
		for j in range(cols):
			result[i][j] = matrix[i][j] * mod

	return result


def kmod(matrix, mod):
	rows = len(matrix)
	cols = len(matrix[0])
	result = [[0 for _ in range(cols)] for _ in range(rows)]

	for i in range(rows):
		for j in range(cols):
			result[i][j] = matrix[i][j] % mod

	return result


def inmatran(k):
	for r in k:
		for j in r:
			print(j, end=' ')
		print()


s = input("Nhập S:")
if len(s) % 2 == 1:
	s += "A"
	idx = 1
else:
	idx = 0
a = ""
b = ""
c = ""
t = ""
k = []
nk = [[0, 0], [0, 0]]
g = ""
s = s.replace(" ", "")
s = s.upper()


print("Nhập các phần tử của ma trận k: ")
for i in range(2):
	r = []
	for j in range(2):
		pt = int(input("Nhập phần tử [{},{}]: ".format(i, j)))
		r.append(pt)
	k.append(r)
detk = (k[0][0] * k[1][1] - k[1][0] * k[0][1])
print("det(K): ", detk)
detk = (k[0][0] * k[1][1] - k[1][0] * k[0][1]) % 26
print("GCD của det(k) và Z là: ", math.gcd(detk, 26))
if math.gcd(detk, 26) != 1:
	print("Lỗi chương trình! K không thể là khóa")
	sys.exit()
for i in range(0, len(s), 2):
	if s[i].isalpha():
		so1 = ((ord(s[i]) - 65) * k[0][0] + (ord(s[i+1]) - 65) * k[1][0])
		so2 = ((ord(s[i]) - 65) * k[0][1] + (ord(s[i+1]) - 65) * k[1][1])
		t = " " + str(so1) + " " + str(so2)
	a += t
print("Dãy số sau khi nhân với k: ", a)
for i in range(0, len(s), 2):
	if s[i].isalpha():
		so3 = (((ord(s[i]) - 65) * k[0][0] +(ord(s[i+1]) - 65) * k[1][0]) % 26)
		so4 = (((ord(s[i]) - 65) * k[0][1] +(ord(s[i+1]) - 65) * k[1][1]) % 26)
		t = " " + str(so3) + " " + str(so4)
	b += t
print("Dãy số sau khi mod Z: ", b)
for i in range(0, len(s), 2):
	if s[i].isalpha():
		ktmh1 = chr((((ord(s[i]) - 65) * k[0][0] + (ord(s[i+1]) - 65) * k[1][0]) % 26) + 65)
		ktmh2 = chr((((ord(s[i]) - 65) * k[0][1] + (ord(s[i+1]) - 65) * k[1][1]) % 26) + 65)
		t = ktmh1+ktmh2
	c += t
print("Chuỗi sau khi mã hóa: ", c)

nk[0][0], nk[1][1] = k[1][1], k[0][0]
nk[0][1], nk[1][0] = -k[0][1], -k[1][0]


kp = pow(detk, -1, 26)
print("nghịch đảo của det(K): ", kp)
knd = kmod(nk, 26)
print("Ma trận k phụ hợp sau khi mod 26: ")
inmatran(knd)
kgm = kadd(knd, kp)
print("Ma trận K-1 sau khi nhân với det(K): ")
inmatran(kgm)
kgm = kmod(kgm, 26)
print("Ma trận K-1")
inmatran(kgm)
# kgm = kmod(kadd(knd,kp),26)
for i in range(0, len(c), 2):
	if c[i].isalpha():
		ktmh1 = chr((((ord(c[i]) - 65) * kgm[0][0] + (ord(c[i+1]) - 65) * kgm[1][0]) % 26) + 65)
		ktmh2 = chr((((ord(c[i]) - 65) * kgm[0][1] + (ord(c[i+1]) - 65) * kgm[1][1]) % 26) + 65)
		t = ktmh1+ktmh2
	g += t
print("Chuỗi sau khi giải mã: ", g)
if idx == 1:
	g = g[:len(g)-1]
print("Chuỗi sau khi cắt các phần tử thừa: ", g)
