class MedianFinder:

    def __init__(self):
        self.nums = []
        self.heap = []

    def addNum(self, num: int) -> None:
        if not self.heap or num <= -self.heap[0]:
            heappush(self.heap, -num)
        else:
            heappush(self.nums, num)

        if len(self.heap)  > len(self.nums)  + 1:
            heappush(self.nums, -heappop(self.heap))
        elif len(self.nums) > len(self.heap):           
            heappush(self.heap, -heappop(self.nums))

            
    def findMedian(self) -> float:
        if len(self.heap) == len(self.nums):
            return (-self.heap[0] + self.nums[0])/2
        else:
            return -self.heap[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()