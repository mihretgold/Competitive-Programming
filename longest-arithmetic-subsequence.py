class Solution:   
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        length = len(nums)
        maxi = 2

        for end in range(length):
            for start in range(end):
                difference = nums[end] - nums[start]
                dp[(end, difference)] = dp[(start, difference)] + 1
                maxi = max(maxi, dp[(end, difference)])

        return maxi