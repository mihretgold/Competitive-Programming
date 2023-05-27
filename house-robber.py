class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = defaultdict(int)
        def calcRobber(index):
            if index == len(nums) - 1:
                return nums[index]
            
            if index >= len(nums):
                return 0
            
            if index in mem:
                return mem[index]

            left = calcRobber(index + 1)
            rigth = calcRobber(index + 2) + nums[index]
            
            mem[index] =  max(left, rigth)
            return mem[index]

        return calcRobber(0)