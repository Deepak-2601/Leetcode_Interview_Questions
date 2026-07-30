def majority_element(arr, target):
    n = len(arr)
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1

    if count > n/2:
        return True
    else:
        return False


nums = [2,4,5,5,5,5,5,6,6] 
target = 5
print(majority_element(nums,target))
