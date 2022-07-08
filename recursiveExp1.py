def exp2(x, n):
    if n == 0:
        return 1
    else:
        return x * exp2(x, n - 1)

x = int(input())
n = int(input())
print(x, n)