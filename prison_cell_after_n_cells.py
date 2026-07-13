def prison_after_n_days(cells, n):
    seen = {}
    while n > 0:
        state_tuple = tuple(cells)
        if state_tuple in seen:
            n %= seen[state_tuple] - n
        seen[state_tuple] = n
        if n >= 1:
            n -= 1
            new_cells = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = new_cells
    return cells


cells = [0, 1, 0, 1, 1, 0, 0, 1]
n = 7
print(prison_after_n_days(cells, n))