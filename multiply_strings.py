def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    result = [0] * (len(num1) + len(num2))
    num1 = num1[::-1]
    num2 = num2[::-1]
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            product = digit1 * digit2
            result[i + j] += product
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(map(str, result[::-1]))

num1 = "123"
num2 = "456"
result = multiply(num1, num2)
print("The product of {} and {} is: {}".format(num1, num2, result))
