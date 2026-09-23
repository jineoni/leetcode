class MyHashMap:

    def __init__(self):
        self.bucket = 10007
        self.hashmap = [[] for _ in range(self.bucket)]

    def put(self, key: int, value: int) -> None:
        index = key % self.bucket
        if self.hashmap[index]:
            for pair in self.hashmap[index]:
                if pair[0] == key:
                    self.hashmap[index].remove(pair)
        
        self.hashmap[index].append((key, value))
        
    def get(self, key: int) -> int:
        index = key % self.bucket
        for pair in self.hashmap[index]:
            if pair[0] == key: return pair[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.bucket
        for pair in self.hashmap[index]:
            if pair[0] == key:
                self.hashmap[index].remove(pair)

# class MyHashMap:

#     def __init__(self):
#         self.hashmap = [-1] * (10**6+1)

#     def put(self, key: int, value: int) -> None:
#         self.hashmap[key] = value
        
#     def get(self, key: int) -> int:
#         return self.hashmap[key]

#     def remove(self, key: int) -> None:
#         self.hashmap[key] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)