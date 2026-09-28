def maxBottles(numBottles,numExchange):
    total_drunk = numBottles 
    empty_bottles = numBottles 
    while empty_bottles >= numExchange:
        new_full_bottles = empty_bottles // numExchange  
        total_drunk += new_full_bottles  
        empty_bottles = empty_bottles % numExchange + new_full_bottles  
    return total_drunk



numBottles = 9
numExchange = 3
result = maxBottles(numBottles, numExchange)
print(result)