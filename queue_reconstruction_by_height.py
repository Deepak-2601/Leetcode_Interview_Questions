def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    queue = []
    for person in people:
        queue.insert(person[1], person)
    return queue

p = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(p))
