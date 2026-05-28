def max_number_of_apples(weight):
    weight.sort()
    total_weight = 0
    count = 0
    for w in weight:
        if total_weight + w <= 5000:
            total_weight += w
            count += 1
        else:
            break
    return count

weights = [100,200,150,1000]
result = max_number_of_apples(weights)
print(result)