class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length     

        for index in range(length):
            maxx = 0
            for idx in range(index - 1, -1, -1):
                if nums[idx] < nums[index]:
                    maxx = max(dp[idx], maxx)

            dp[index] += maxx

        return max(dp)

        