def fact(n):    # 재귀
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

n = int(input())
print(fact(n))