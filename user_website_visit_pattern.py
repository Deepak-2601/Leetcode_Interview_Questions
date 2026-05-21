def mostVisitedPattern(username, timestamp, website):
    from collections import defaultdict
    from itertools import combinations
    
    user_visits = defaultdict(list)
    
    for u, t, w in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
        user_visits[u].append(w)
    
    pattern_count = defaultdict(int)
    
    for visits in user_visits.values():
        unique_patterns = set(combinations(visits, 3))
        for pattern in unique_patterns:
            pattern_count[pattern] += 1
    
    max_score = max(pattern_count.values())
    most_visited = [pattern for pattern, count in pattern_count.items() if count == max_score]
    
    return min(most_visited)

username = ["joe","joe","joe","james","james","james","james","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9]
website = ["home","about","career","home","cart","maps","home","home","about"]
print(mostVisitedPattern(username, timestamp, website)) 