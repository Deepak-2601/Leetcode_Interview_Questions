def matrixBlockSum(mat, k):
    m, n = len(mat), len(mat[0])
    answer = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            # Calculate the sum for the block centered at (i, j)
            for r in range(max(0, i - k), min(m, i + k + 1)):
                for c in range(max(0, j - k), min(n, j + k + 1)):
                    answer[i][j] += mat[r][c]
    return answer

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
result = matrixBlockSum(mat, k)
for row in result:
    print(row)