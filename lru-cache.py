class LRUCache:

    def __init__(self, capacity: int):
        self.store = defaultdict(int)
        self.capacity = capacity
        
        
    def get(self, key: int) -> int:
        if key in self.store:
            value = self.store.pop(key)
            self.store[key] = value
            return value

        return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)

        elif len(self.store) >= self.capacity:
            for num in self.store:
                self.store.pop(num)
                break


        self.store[key] = value
        



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)