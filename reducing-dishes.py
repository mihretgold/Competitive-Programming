class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int: 
        length = len(satisfaction)
        dp = [0] * length
        satisfaction.sort(reverse = True)

        for row in range(length):
            val = 1 * satisfaction[row]
            count = 2
            for col in range(row-1, -1, -1):
                val += count * satisfaction[col]
                count += 1

            if val < 0:
                val = 0
            dp[row] = val

        return max(dp)