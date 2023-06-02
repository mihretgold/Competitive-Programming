class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = defaultdict(int)
        def calTarget(sums, index):
            if index >= len(nums):
                if sums == target:
                    return 1
                else:
                    return 0

            if (sums, index) in mem:
                return mem[(sums, index)]

            left = calTarget(sums - nums[index], index+1)
            right = calTarget(sums + nums[index], index + 1)

            mem[(sums, index)]  = left + right
            return mem[(sums, index)]

        return calTarget(0, 0)