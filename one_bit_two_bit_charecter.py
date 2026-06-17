def isOneBitCharacter(bits):
    n = len(bits)
    i = 0
    while i < n - 1:
        if bits[i] == 0:
            i += 1
        else:
            i += 2
    return i == n - 1


bits = [1, 0, 0]
print(isOneBitCharacter(bits))