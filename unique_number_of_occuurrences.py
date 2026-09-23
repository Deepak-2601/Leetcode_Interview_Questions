def uniqueOccurrences(arr):
    from collections import Counter
    counts = Counter(arr)
    occurrences = list(counts.values())
    return len(occurrences) == len(set(occurrences))

arr = [1, 2, 2, 1, 1, 3]
print(uniqueOccurrences(arr))