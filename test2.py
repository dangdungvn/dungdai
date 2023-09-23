list_nums = input()
list_nums = list_nums.split(" ")
list_nums = list(map(int,list_nums))
dem = 0

for i in range(1, list_nums[0]+1):
    if i % list_nums[1] == 0 or i % list_nums[2] == 0 or i % list_nums[3] == 0:
        dem +=1
print(dem)