def subtractProductAndSum(n):
    product = 1
    sum_digits = 0
    for digit in str(n):
        d = int(digit)
        product *= d
        sum_digits += d
    return product - sum_digits


n = 234
result = subtractProductAndSum(n)   
print(result)