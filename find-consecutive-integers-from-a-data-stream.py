class DataStream:

    def __init__(self, value: int, k: int):
        self.size = k
        self.val = value
        self.count = 0

    def consec(self, num: int) -> bool:
        
        if num == self.val:
            self.count += 1
        else:
            self.count = 0
        self.count = min(self.size, self.count) 
        
        return self.count == self.size
            

        



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)