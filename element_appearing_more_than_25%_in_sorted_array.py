def findSpecialInteger(arr):
    n = len(arr)
    threshold = n // 4
    for i in range(n):
        if i + threshold < n and arr[i] == arr[i + threshold]:
            return arr[i]
    return None  

arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
result = findSpecialInteger(arr)
print(result) 