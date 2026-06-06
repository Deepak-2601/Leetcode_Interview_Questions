def fixedPoint(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1

arr = [-10, -5, 0, 3, 7]
print(fixedPoint(arr))