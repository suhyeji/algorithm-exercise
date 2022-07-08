def bubbleSort(arr, n): #인접한 두 수 비교
    for i in range(n - 1, 0, -1):
        sorted = True
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        if sorted:
            return arr

arr = list(map(int, input().split()))
print(bubbleSort(arr, len(arr)))