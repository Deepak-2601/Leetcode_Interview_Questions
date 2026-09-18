def shipWithinDays(weights, days):
    def canShip(capacity):
        current_weight = 0
        days_needed = 1
        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = 0
            current_weight += weight
        return days_needed <= days
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        if canShip(mid):
            right = mid
        else:
            left = mid + 1
    return left

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
result = shipWithinDays(weights, days)
print(result)
