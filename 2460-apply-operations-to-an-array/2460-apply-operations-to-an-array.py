class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)
        right = 0
        left = 0
        for index in range(length-1):
            if nums[index] ==nums[index + 1]:
                nums[index] = 2*nums[index]
                nums[index + 1] = 0
                
        while right < length:
            if nums[right] == 0:
                right += 1
            else:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left += 1
                right += 1
        
        return nums