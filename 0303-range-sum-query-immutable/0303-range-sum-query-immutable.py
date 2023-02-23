class NumArray:

    def __init__(self, nums: List[int]):
        length = len(nums)
        self.prefix = [0 for _ in range(length+1)]
        for i in range(1, length + 1):
            self.prefix[i] = self.prefix[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        sums = self.prefix[right+1] - self.prefix[left]
        
        return sums


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)