def numberOfSteps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps

n = 14
result = numberOfSteps(n)
print(f"Number of steps to reduce {n} to zero: {result}")
