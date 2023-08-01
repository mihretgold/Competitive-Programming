class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        start = 0
        length = len(nums)
        end = 0
        maxi = 0

        for end in range(length):
            while start < length and (nums[start] % 2 != 0 or nums[start] > threshold):
                start += 1

            if end > start and (nums[end] % 2 == nums[end-1] % 2 or nums[end] > threshold):
                start = end

            if start <= end:
                maxi = max(maxi, end - start + 1)

        return maxi