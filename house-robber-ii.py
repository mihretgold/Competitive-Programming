class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 1:
            return nums[0]

        dp = [0]*length
        for index in range(length-1, 0, -1):
            if index + 2 < length:
                dp[index] = max(dp[index], dp[index + 2])

            if index + 3 < length:
                dp[index] = max(dp[index], dp[index + 3])

            dp[index] += nums[index]

        maxi = max(dp)
        dp = [0]*length
        for index in range(length-2, -1, -1):
            if index + 2 < length:
                dp[index] = max(dp[index], dp[index + 2])

            if index + 3 < length:
                dp[index] = max(dp[index], dp[index + 3])

            dp[index] += nums[index]

        maxi = max(maxi, max(dp))
        return maxi