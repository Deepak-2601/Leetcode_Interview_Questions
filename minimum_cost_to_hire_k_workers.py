import heapq
def mincostToHireWorkers(quality, wage, k):
    workers = sorted([(w / float(q), q, w) for q, w in zip(quality, wage)])
    res = float('inf')
    total_quality = 0
    max_heap = []    
    for ratio, q, w in workers:
        total_quality += q
        heapq.heappush(max_heap, -q)
        if len(max_heap) > k:
            total_quality += heapq.heappop(max_heap)
        if len(max_heap) == k:
            res = min(res, ratio * total_quality)         
    return res

quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
result = mincostToHireWorkers(quality, wage, k)
print(result)