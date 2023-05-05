class KthLargest:

    def __init__(self, k: int, nums: List[int]):   
        self.num = nums
        self.K = k     
        heapify(self.num)      
        while len(self.num) > self.K:
            heappop(self.num)


    def add(self, val: int) -> int:
        heappush(self.num, val)
        if len(self.num) > self.K:
            heappop(self.num)

        return self.num[0]
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)