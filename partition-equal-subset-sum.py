class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) 
        length = len(nums)
        if target & 1 != 0:
            return False

        target //= 2


        dp = set()
        dp.add(0)

        for index in range(length):
            nextdp = set()
            for val in dp:
                if val + nums[index] == target:
                    return True
                nextdp.add(val + nums[index])
                nextdp.add(val)

            dp = nextdp

        return False