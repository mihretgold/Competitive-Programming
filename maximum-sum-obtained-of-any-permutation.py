class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length = len(nums)
        prefix = [0 for _ in range(length)]
        for a, b in requests:
            prefix[a] += 1
            if b < length-1:
                prefix[b+1] -= 1
        
        for index in range(1, length):
            prefix[index] += prefix[index-1]

        prefix.sort()
        nums.sort()
        sums = 0

        for index in range(length):
            print(prefix[index], nums[index])
            sums += (prefix[index] * nums[index])

        return sums