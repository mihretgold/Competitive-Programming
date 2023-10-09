class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        length2 = len(nums2)
        maxGlobal = 0

        dp = [[0 for _ in range(length + 1)] for _ in range(length2 + 1)]

        for row in range(length2-1, -1, -1):
            for col in range(length - 1, -1, -1):
                if nums2[row] == nums1[col]:
                    dp[row][col] += 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] += max(dp[row + 1][col], dp[row][col + 1])

                maxGlobal = max(dp[row][col], maxGlobal)

        return maxGlobal