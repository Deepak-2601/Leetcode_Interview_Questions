def maxKilledEnemies(grid):
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    max_kills = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '0':
                kills = 0
                for k in range(j, n):
                    if grid[i][k] == 'W':
                        break
                    if grid[i][k] == 'E':
                        kills += 1
                for k in range(j - 1, -1, -1):
                    if grid[i][k] == 'W':
                        break
                    if grid[i][k] == 'E':
                        kills += 1
                for k in range(i, m):
                    if grid[k][j] == 'W':
                        break
                    if grid[k][j] == 'E':
                        kills += 1
                for k in range(i - 1, -1, -1):
                    if grid[k][j] == 'W':
                        break
                    if grid[k][j] == 'E':
                        kills += 1
                max_kills = max(max_kills, kills)
    return max_kills

grid = [
    ['0', 'E', '0', '0'],
    ['E', '0', 'W', 'E'],
    ['0', 'E', '0', '0'],
]
result = maxKilledEnemies(grid)
print(result)