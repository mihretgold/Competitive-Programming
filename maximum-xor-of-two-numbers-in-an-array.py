class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxx = 0
        mask = 0
        size = len(bin(max(nums))) - 1 

        for i in range(size, -1, -1):
            mask |= (1 << i)
            newmask = maxx | (1 << i)

            xorSet = set( num & mask for num in nums)

            for prefix in xorSet:
                if prefix ^ newmask in xorSet:
                    maxx = newmask

            xorSet.clear()
                    

        return maxx