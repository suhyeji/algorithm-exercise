def insertionSort(arr, n):  # arr[i]를 포함하여 정렬
    for i in range(1, n):
        temp = arr[i]
        insert = i
        for j in range(i - 1, -1, -1):
            if arr[j] > temp:
                arr[j + 1] = arr[j]
                insert = j
            else:
                break
        arr[insert] = temp
    return arr
        
arr = list(map(int, input().split()))
print(insertionSort(arr, len(arr)))