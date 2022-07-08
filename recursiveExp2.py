def exp3(x, n): #재귀
    if n == 0:
        return 1
    elif n % 2 == 0:  # n이 짝수 : ( x ^ (n/2) )^2
        return exp3(x * x, n / 2)
    else:           # n이 홀수 : x * (x^2) ^ (n-1)/2
        return x * exp3(x * x, (n - 1) / 2)

x = int(input())
n = int(input())
print(exp3(x, n))