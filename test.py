list_nums = input()
list_nums = list_nums.split(" ")
list_nums = list(map(int, list_nums))
s = 0
k = list_nums[0]
n = list_nums[1] % 1000 + 1
for i in range(1, n):
    if i >= 100:
        i = str(i)[-2:]
        i = int(i)
    if k >= 100:
        k = str(k)[-2:]
        k = int(k)

    n = pow(2, k)
    n = str(n)[-2:]
    n = int(n)

    m = pow(i, n)
    m = str(m)[-2:]
    m = int(m)

    s += m
    s = str(s)[-2:]
    s = int(s)
if s < 10:
    s = "{:02d}".format(s)
print(s)