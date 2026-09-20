def calcEquation(equations, values, queries):
    from collections import defaultdict
    graph = defaultdict(dict)
    for (A, B), value in zip(equations, values):
        graph[A][B] = value
        graph[B][A] = 1 / value

    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)
        for neighbor, value in graph[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * value
        return -1.0

    results = []
    for C, D in queries:
        results.append(dfs(C, D, set()))
    return results

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
result = calcEquation(equations, values, queries)
print(result)
