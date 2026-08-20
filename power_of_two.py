def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

n = 16
result = isPowerOfTwo(n)
print(f"Is {n} a power of two? {result}.")