def heightChecker(heights):
    expected = sorted(heights)
    mismatch_count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            mismatch_count += 1
    return mismatch_count

height = [1, 1, 4, 2, 1, 3]
result = heightChecker(height)
print(result)