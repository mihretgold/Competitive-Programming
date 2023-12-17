class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        maxi = nums[-1]
        sums = nums[-1]

        for index in range(length - 2, -1, -1):  
            if (sums + nums[index]) > nums[index]:
                sums = nums[index] + sums
            else:
                sums = nums[index]
            maxi = max(maxi, sums)

        return maxi