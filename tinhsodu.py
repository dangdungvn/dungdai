sum = 1
m = int(input("Nhập vào lũy thừa: "))
n = int(input("Nhập vào số mũ: "))
k = int(input("Nhập vào số bị chia: "))
for i in range(n):
	sum*=m
sum = sum % k
print(sum)