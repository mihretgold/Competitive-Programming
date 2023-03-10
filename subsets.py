class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        path = []
        def calcSubsets(index, path):
            if index == len(nums):
                subsets.append(path[:])
                return

            path.append(nums[index])
            calcSubsets(index+1, path)
            path.pop()
            calcSubsets(index+1, path)

        calcSubsets(0, path)
        return subsets