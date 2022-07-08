def binarySearch(arr, item, left, right): # 재귀
    if left <= right:
        mid = (left + right) / 2
        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            return binarySearch(arr, item, left, mid - 1)
        else:
            return binarySearch(arr, item, mid + 1, right)
    else:
        return -1

arr = list(map(int, input().split()))
item = int(input())
print(binarySearch(arr, item, 0, len(arr) - 1))