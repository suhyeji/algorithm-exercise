def maximum(arr, first, last):  # 분할과 정복
    if first == last:
        return arr[first]
    else:
        mid = (first + last) // 2
        lmax = maximum(arr, first, mid)
        rmax = maximum(arr, mid + 1, last)

        if lmax > rmax:
            return lmax
        else:
            return rmax

arr = list(map(int, input().split()))
print(maximum(arr, 0, len(arr) - 1))