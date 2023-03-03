class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        sums = 0 
        for num in nums:
            prefix += num
            if prefix - goal in count:
                sums += count[prefix-goal]
            count[prefix] += 1
        return sums