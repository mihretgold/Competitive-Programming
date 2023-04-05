class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        length = (2**len(nums))
        xors = defaultdict(int)

        for index in range(length):
            temp = 0
            for i in range(len(nums)):
                if index & 1 << i != 0:
                    val = nums[i]
                    temp |= val
            xors[temp] += 1
        
        maxi = 0
        for num in xors:
            maxi = max(maxi, xors[num])

        
        return maxi