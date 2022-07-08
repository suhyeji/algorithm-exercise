def rebuildHeap(arr, root, n):
    current = root
    value = arr[root]    # 루트 값을 value에 저장
    while (2 * current + 1 < n):  # current != leaf
        leftChild = 2 * current + 1
        rightChild = leftChild + 1
        # 두 자식 노드 중 큰 값을 largerChild로 둠
        if rightChild < n and arr[rightChild] > arr[leftChild]:
            largerChild = rightChild
        else:
            largerChild = leftChild

        if value < arr[largerChild]:
            arr[current] = arr[largerChild]
            current = largerChild
        else:
            break
    arr[current] = value

def heapSort(arr):
    n = len(arr)
    # 1. 최대힙 만들기
    # 마지막 노드의 부모 노드부터 시작
    for i in range((n // 2) - 1, -1, -1):
        rebuildHeap(arr, i, n)

    # 2. 정렬하기
    # 최대 원소를 마지막으로 옮기고
    # A[0] ~ A[last - 1]을 최대힙으로 만듦
    heapSize = n
    for last in range(n - 1, 0, -1):
        arr[0], arr[last] = arr[last], arr[0]
        heapSize -= 1
        rebuildHeap(arr, 0, heapSize)

    return arr

arr = list(map(int, input().split()))
print(heapSort(arr))