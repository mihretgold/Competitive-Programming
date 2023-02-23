class NumArray:

    def __init__(self, nums: List[int]):
        length = len(nums)
        self.prefix = list(accumulate(nums))
        self.prefix.insert(0,0)
    def sumRange(self, left: int, right: int) -> int:
        sums = self.prefix[right+1] - self.prefix[left]
        
        return sums


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)