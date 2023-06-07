class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        length = len(arr)

        for i in range(length):
            if (arr[i] - difference) in dp:
                dp[arr[i]] = dp[arr[i] - difference] + 1
            else:
                dp[arr[i]] = 1

        result = max(dp.values())
        return result