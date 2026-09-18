def sorted_squares(nums):
    squares = []
    for num in nums:
        squares.append(num * num)
    squares.sort()
    return squares

n = [-4, -1, 0, 3, 10]
result = sorted_squares(n)
print(result)