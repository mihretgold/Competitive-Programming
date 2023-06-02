class Solution:
    def minDifference(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 3:
            return 0

        nums.sort()
        result1 = nums[length-4] - nums[0]
        result2 = nums[length-1] - nums[3]
        result3 = nums[length-2] - nums[2]
        result4 = nums[length-3] - nums[1]
        result = min(result1, result2, result3, result4) 
        return result