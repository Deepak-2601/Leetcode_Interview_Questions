def selfDividingNumbers(left, right):
    result = []
    for num in range(left, right + 1):
        if isSelfDividing(num):
            result.append(num)
    return result

def isSelfDividing(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for digit in str_num:
        if num % int(digit) != 0:
            return False
    return True

left = 1
right = 22
print(selfDividingNumbers(left, right))
