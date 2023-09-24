import math
def count_divisors(n):
    count = 1
    sqrt_n = int(math.sqrt(n))
    
    # Phân tích n thành các số nguyên tố mũ
    for i in range(2, sqrt_n + 1):
        power = 0
        while n % i == 0:
            n //= i
            power += 1
        count *= (power + 1)
    
    # Xử lý trường hợp n là một số nguyên tố lớn hơn sqrt(n)
    if n > 1:
        count *= 2
    
    return count

n = int(input())
print(count_divisors(n))