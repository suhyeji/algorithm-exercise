n = 8
d = 1
numList = [10, 30, 35, 40, 45, 65, 70, 80]
n = len(numList)
k = 0
maxNum = 0
for i in range(n):
    while (k < n and numList[k] - numList[i] <= d):
        k += 1
    if maxNum < k - i:
        maxNum = k - i
    if k == n:
        break
print(maxNum)