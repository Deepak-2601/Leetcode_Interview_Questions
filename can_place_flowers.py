def selfDividingNumbers(left, right):
    result = []
    for num in range(left, right + 1):
        if '0' in str(num):
            continue
        if all(num % int(digit) == 0 for digit in str(num)):
            result.append(num)
    return result


left = 1
right = 22
print(selfDividingNumbers(left, right))