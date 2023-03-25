class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # answer = []
        length = len(nums)
        i = 0
        while i < length:
            correct_position = nums[i] - 1
            if i != correct_position and nums[correct_position] != nums[i]:
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1 
        

        return nums[-1]