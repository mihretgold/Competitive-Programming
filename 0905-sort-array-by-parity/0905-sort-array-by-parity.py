class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        right = 0
        left = 0
        length = len(nums)
        while right < length:
            if nums[right] % 2 != 0:
                right += 1
            else:
                temp = nums[right];
                nums[right] = nums[left]
                nums[left] = temp
                right += 1
                left += 1
        
        return nums