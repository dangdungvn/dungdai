
def demsolaplai(list,n):
	dem = 0
	for i in list:
		if i == n:
			dem +=1
	return dem 

def inlist(a):
	for i in a:
		print(i, end ='  ')
	print("")
a = input()
b = []
c = [" "]
d = ["    "]



a = list(a)

b.extend(a[0]*3)
c.extend(a[1]*2)
d.extend(a[2])

inlist(a)
inlist(b)
inlist(c)
inlist(d)
