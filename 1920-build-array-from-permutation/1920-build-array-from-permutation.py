class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        for index in range(length):
            ans.append(nums[nums[index]])
        
        return ans