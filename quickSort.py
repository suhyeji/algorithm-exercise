import random

def quickSort(arr, minIndex, maxIndex):
    if minIndex < maxIndex:
        pivot = partition(arr, minIndex, maxIndex)
        quickSort(arr, minIndex, pivot - 1)
        quickSort(arr, pivot + 1, maxIndex)
        
    return arr


def partition(arr, minIndex, maxIndex):
    index = random.randint(minIndex, maxIndex)
    pivot = arr[index]

    arr[index], arr[minIndex] = arr[minIndex], arr[index]

    i = minIndex + 1
    j = maxIndex

    while i <= j:
        while (i <= maxIndex and arr[i] < pivot):
            i += 1
        while (j >= minIndex + 1 and arr[j] >= pivot):
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[minIndex], arr[j] = arr[j], arr[minIndex]
    return j 

arr = list(map(int, input().split()))
print(quickSort(arr, 0, len(arr) - 1))