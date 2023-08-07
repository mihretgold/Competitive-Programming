class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        def EvenOdd(a, b):
            return (a & 1) != (b & 1)
        start = 0
        length = len(nums)
        end = 0
        maxi = 0

        for end in range(length):
            if end > 0 and EvenOdd(nums[end], nums[end-1]) and max(nums[end], nums[end-1]) <= threshold:
                start += 1
            else: 
                val = nums[end] % 2 == 0 and nums[end] <= threshold
                if val:
                    start = 1
                else:
                    start = 0

            
            maxi = max(maxi,  start)

        return maxi
