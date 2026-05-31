def distributeCandies(candyType):
    unique_candies = set(candyType)
    max_candies_to_eat = len(candyType) // 2
    return min(len(unique_candies), max_candies_to_eat)

candyType = [1, 1, 2, 2, 3, 3]
print(distributeCandies(candyType))
