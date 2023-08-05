class Solution: 
    def permute(self, nums: List[int]) -> List[List[int]]:
        unique = set()
        result = []
        def calcPermute(unique, path):
            if len(path) == len(nums):
                result.append(path[:])

            for index in range(len(nums)):
                if nums[index] not in unique:
                    path.append(nums[index])
                    unique.add(nums[index])
                    calcPermute(unique, path[:])
                    path.pop()
                    unique.remove(nums[index])

        
        calcPermute(unique, [])
        return result