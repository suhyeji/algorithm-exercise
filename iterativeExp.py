def exp1(x, n): # 반복 / x^n
    result = 1
    for i in range(1, n + 1):
        result *= x
    return result

x = int(input())
n = int(input())
print(x, n)