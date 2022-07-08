def selectionSort(arr, n):  #가장 큰 원소를 맨 뒤로 보내기
    for i in range(n - 1, -1, -1):
        # a[0]부터 a[i]까지 가장 큰 원소의 위치를 찾는다.
        index = 0
        for j in range(1, i + 1):  
            if arr[index] < arr[j]:
                index = j

        # a[index]와 a[i]를 교환한다.
        arr[index], arr[i] = arr[i], arr[index]

    return arr

arr = list(map(int, input().split()))
print(selectionSort(arr, len(arr)))