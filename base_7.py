def convertToBase7(num):
    if num == 0:
        return "0"
    is_negative = num < 0
    num = abs(num)
    base7 = ""
    while num > 0:
        base7 = str(num % 7) + base7
        num //= 7    
    return "-" + base7 if is_negative else base7

num = 100
print(convertToBase7(num))
