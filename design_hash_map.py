class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def put(self, key, value):
        index = key % self.size
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))

    def get(self, key):
        index = key % self.size
        for k, v in self.map[index]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        index = key % self.size
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                del self.map[index][i]
                return
            
hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)          
print(hashMap.get(1))     