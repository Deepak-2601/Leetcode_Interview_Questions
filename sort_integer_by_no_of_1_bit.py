def sortByBits(arr):
    def count_ones(n):
        return bin(n).count('1')
    arr.sort(key=lambda x: (count_ones(x), x))
    return arr

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = sortByBits(arr)
print(result)