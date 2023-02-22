class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        sum = 0
        for i in range(length):
            sum += nums[i]
        p = 0
        for i in range(length):
            check = sum - p - nums[i]
            if check == p:
                return i
            p += nums[i]
        
        return -1