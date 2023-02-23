class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = float('-inf')
        length = len(nums)
        start = 0
        sums = 0
        for end in range(length):
            sums += nums[end]
            if end - start + 1 == k:
                avg = sums/k
                maxi = max(maxi, avg)
                sums -= nums[start]
                start += 1
                
        return maxi