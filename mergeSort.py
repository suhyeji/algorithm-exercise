def mergeSort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2

    leftList = mergeSort(arr[:mid])
    rightList = mergeSort(arr[mid:])

    return merge(leftList, rightList)

def merge(list1, list2):
    n1 = len(list1)
    n2 = len(list2)
    
    mergedList = [0] * (n1 + n2)
    
    i, j, k = 0, 0, 0
    
    while i < n1 and j < n2:
        if list1[i] <= list2[j]:
            mergedList[k] = list1[i]
            i += 1
            k += 1
        else:
            mergedList[k] = list2[j]
            j += 1
            k += 1
            
    while i < n1:
        mergedList[k] = list1[i]
        i += 1
        k += 1

    while j < n2:
        mergedList[k] = list2[j]
        j += 1
        k += 1

    return mergedList

num = int(input())
arr = list(map(int, input().split()))

print(mergeSort(arr, num))
