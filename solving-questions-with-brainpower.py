class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0]*length
        maxArr = [0]*(length+1)

        for index in range(length-1, -1, -1):
            dp[index] += questions[index][0]
            if index + questions[index][1] + 1 < length:
                dp[index] += maxArr[index + questions[index][1] + 1]
            maxArr[index] = max(maxArr[index+1], dp[index])

        maxi = max(dp)
        return maxi