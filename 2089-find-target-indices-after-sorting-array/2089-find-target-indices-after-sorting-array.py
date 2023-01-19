class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        nums.sort()
        # bottom = 0
        # top = length - 1
        answer = []
        for index in range(length):
            if nums[index] == target:
                answer.append(index)
                
        return answer