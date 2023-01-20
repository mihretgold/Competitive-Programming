class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = 0
        count_one = 0
        count_two = 0
        for num in nums:
            if num == 0:
                count_zero += 1
            elif num == 1:
                 count_one += 1
            elif num == 2:
                count_two += 1
        
        for index in range(count_zero):
            nums[index] = 0
        
        size = count_zero + count_one
        for index in range(count_zero, size):
            nums[index] = 1
            
        length = len(nums)
        for index in range(size, length):
            nums[index] = 2