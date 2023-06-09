class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = defaultdict(int)
        def calc(currSum):
            if currSum == target:
                return 1
            if currSum > target:
                return 0
            if currSum in mem:
                return mem[currSum]

            sums = 0
            for index in range(len(nums)):
                sums += calc(currSum + nums[index])

            mem[currSum] = sums
            return mem[currSum]
        return calc(0)