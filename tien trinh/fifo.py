def incach(a):
	for i in range(len(a)):
		print("P{}".format(i+1)+" "*a[i]*2,end = "")
	print("")
	for i in range(len(a)):
		print("_"*a[i]*2,end = " |")
	print("")
	for i in range(len(a)):
		if a[i] >= 10:
			print("{}".format(a[i]) + " " * (a[i] * 2 - 1), end = " ")
		else:
			print("{}".format(a[i]) + " " * a[i] * 2, end = " ")
	print("")

def tgcho(a,b):
	res = []
	for i in range(len(a)):
		if i == 0:
			res.append(a[i])
		else:
			res.append(res[i - 1] + a[i])
	res.insert(0,0)
	return res[b-1]

def tongtgcho(a):
	res = []
	sum = 0
	for i in range(len(a)):
		if i == 0:
			res.append(a[i])
		else:
			res.append(res[i - 1] + a[i])
	res.insert(0,0)
	res = res[:-2]
	for i in res:
		sum += i
	return sum


a = []


n = int(input("số tiến trình được thực thi: "))
for i in range(n):
	t = int(input("Thời gian CPU của P{}: ".format(i+1)))
	a.append(t)
print("")
incach(a)
print("")
for i in range(n):
	print("Thời gian chờ của P{}: {}s".format(i+1,tgcho(a,i+1)))
print("Thời gian chờ của {} tiến trình là: ".format(n),tongtgcho(a))
print("Thời gian chờ trung bình của {} tiến trình: ".format(n),tongtgcho(a)/5)