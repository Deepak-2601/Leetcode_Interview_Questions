def two_city_sched_cost(costs):
    n = len(costs) // 2
    costs.sort(key=lambda x: x[0] - x[1])
    total_cost = 0
    for i in range(n):
        total_cost += costs[i][0]  
    for i in range(n, 2 * n):
        total_cost += costs[i][1] 
    return total_cost

c = [[10, 20], [30, 200], [400, 50], [30, 20]]
print(two_city_sched_cost(c))