class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] - 1 <= n and nums[i] - 1 >= 0:
                correct_position = nums[i] - 1
                if i != correct_position:
                    nums[i], nums[correct_position] = nums[correct_position], nums[i]
                else:
                    i += 1
            else:
                i += 1
        
        if 0 in nums:
            return nums.index(0) + 1
        else:
            return 0