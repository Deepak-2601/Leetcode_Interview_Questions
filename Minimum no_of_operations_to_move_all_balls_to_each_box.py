def minOperations(boxes):   
    n = len(boxes)
    answer = [0] * n
    for i in range(n):
        for j in range(n):
            if boxes[j] == '1':
                answer[i] += abs(i - j)
    return answer

boxes = "110"
print(minOperations(boxes))