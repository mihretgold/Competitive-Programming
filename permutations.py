class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        unique = 0
        result = []
        def calcPermute( path):
            nonlocal unique
            if len(path) == len(nums):
                result.append(path[:])

            for index in range(len(nums)):
                if unique & (1 << index) == 0:
                    path.append(nums[index])
                    unique |= 1 << index
                    calcPermute(path[:])
                    path.pop()
                    unique ^= 1 << index

        
        calcPermute([])
        return result