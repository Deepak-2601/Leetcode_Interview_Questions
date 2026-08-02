def findRestaurant(list1, list2):
    index_map = {restaurant: i for i, restaurant in enumerate(list1)}
    min_sum = float('inf')
    result = []

    for j, restaurant in enumerate(list2):
        if restaurant in index_map:
            index_sum = index_map[restaurant] + j
            if index_sum < min_sum:
                min_sum = index_sum
                result = [restaurant]
            elif index_sum == min_sum:
                result.append(restaurant)
    return result

l1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
l2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findRestaurant(l1, l2))