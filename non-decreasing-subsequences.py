class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        def calcSubsequence(index, path):
            if len(path) >= 2 and path not in result:
                result.append(path[:])

            if len(path) == len(nums):
                return 


            for i in range(index, len(nums)):
                if not path or path[-1] <= nums[i]:
                    path.append(nums[i])
                    calcSubsequence(i+1, path[:])
                    path.pop()

        calcSubsequence(0, [])

        return result