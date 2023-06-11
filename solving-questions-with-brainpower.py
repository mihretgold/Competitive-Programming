class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0]*length

        for index in range(length-1, -1, -1):
            dp[index] += questions[index][0]
            if index + questions[index][1] + 1 < length:
                dp[index] += dp[index + questions[index][1] + 1]

        maxi = max(dp)
        return maxi