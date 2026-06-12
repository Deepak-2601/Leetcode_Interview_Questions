def hammingDistance(x, y):
    xor = x ^ y
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count

x = 1
y = 4
print(hammingDistance(x, y))
