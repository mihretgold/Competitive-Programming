class Solution:
    def checkSum(self, nums, threshold, check):
        length = len(nums)
        sums = 0
        for index in range(length):
            sums += ceil(nums[index]/check)

        return sums <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low <= high:
            mid = low + (high - low)//2
            if self.checkSum(nums, threshold, mid):
                high = mid - 1
            else:
                low = mid + 1

        return low