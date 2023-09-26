class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        mem = defaultdict(int)
        def calc(index, currSum):
            if index == len(stones):
                return abs(currSum)

            if (index, currSum) in mem:
                return mem[(index, currSum)]

            left = calc(index + 1, currSum - stones[index])
            right = calc(index + 1, currSum + stones[index])

            mem[(index, currSum)] = min(left, right)
            return mem[(index, currSum)]
        return calc(0, 0)