class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = (2**len(nums))
        subsets = []

        for index in range(length):
            temp = []
            for i in range(len(nums)):
                if index & 1 << i != 0:
                    val = nums[i]
                    temp.append(val)
            subsets.append(temp)



        return subsets