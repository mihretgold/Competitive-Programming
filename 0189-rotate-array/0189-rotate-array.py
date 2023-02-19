class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k%length
        end = (length - k) - 1
        i = 0
        while i < end:
            nums[i] , nums[end] = nums[end], nums[i]
            i += 1
            end -= 1
        
        i = length - k
        end = length - 1
        while i < end:
            nums[i] , nums[end] = nums[end], nums[i]
            i += 1
            end -= 1
        
        end = length - 1
        i = 0
        while i < end:
            nums[i] , nums[end] = nums[end], nums[i]
            i += 1
            end -= 1
        
        