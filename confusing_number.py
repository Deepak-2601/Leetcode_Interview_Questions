def confusingNumber(n):
    valid_digits = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    rotated = ''
    
    for digit in str(n):
        if digit not in valid_digits:
            return False
        rotated = valid_digits[digit] + rotated
    
    return rotated != str(n)

no = 6
print(confusingNumber(no))