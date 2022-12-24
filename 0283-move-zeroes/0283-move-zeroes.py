class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        right = 0
        left =0 
        while(right < length):
            if nums[right] == 0:
                right += 1;
            else:
                temp = nums[right];
                nums[right] = nums[left]
                nums[left] = temp
                right += 1
                left += 1
                