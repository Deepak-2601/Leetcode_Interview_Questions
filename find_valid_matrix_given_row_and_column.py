def restoreMatrix(rowSum, colSum):
    m, n = len(rowSum), len(colSum)
    matrix = [[0] * n for _ in range(m)]    
    for i in range(m):
        for j in range(n):
            val = min(rowSum[i], colSum[j])
            matrix[i][j] = val
            rowSum[i] -= val
            colSum[j] -= val
    return matrix

rowSum = [3, 8]
colSum = [4, 7]
result = restoreMatrix(rowSum, colSum)
print(result)       