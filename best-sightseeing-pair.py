class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        maxi = values[-1]
        length = len(values)

        for index in range(length - 2, -1, -1):
            maxi -= 1
            val = maxi + values[index]
            ans = max(ans, val)
            if values[index] > maxi:
                maxi = values[index]

        return ans