def addToArrayForm(num, k):
    num_int = int(''.join(map(str, num)))
    result_int = num_int + k
    result_array = [int(digit) for digit in str(result_int)]
    return result_array


num = [1, 2, 0, 0]
k = 34
result = addToArrayForm(num, k)
print(result)

