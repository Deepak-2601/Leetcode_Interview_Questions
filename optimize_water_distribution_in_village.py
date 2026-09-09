def minCostToSupplyWater(n, wells, pipes):
    graph = {i: [] for i in range(n + 1)}
    for i in range(1, n + 1):
        graph[0].append((wells[i - 1], i)) 
    for house1, house2, cost in pipes:
        graph[house1].append((cost, house2))
        graph[house2].append((cost, house1))
    import heapq
    min_heap = [(0, 0)]  
    visited = set()
    total_cost = 0
    while min_heap and len(visited) < n + 1:
        cost, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        total_cost += cost
        for edge_cost, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_cost, neighbor))
    return total_cost

n = 3
wells = [1, 2, 2]
pipes = [[1, 2, 1], [2, 3, 1]]
print(minCostToSupplyWater(n, wells, pipes))