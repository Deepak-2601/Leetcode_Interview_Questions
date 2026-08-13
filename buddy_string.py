def canBeEqual(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal:
        return len(set(s)) < len(s)
    diff_indices = [i for i in range(len(s)) if s[i] != goal[i]]
    
    if len(diff_indices) != 2:
        return False
    i, j = diff_indices
    return s[i] == goal[j] and s[j] == goal[i]

s = "ab"
goal = "ba"
print(canBeEqual(s, goal))