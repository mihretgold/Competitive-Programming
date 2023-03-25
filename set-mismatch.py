class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        answer = []
        length = len(nums)
        i = 0
        while i < length:
            correct_position = nums[i] - 1
            if i != correct_position and nums[correct_position] != nums[i]:
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1

    
        for index, num in enumerate(nums):
            if num != (index + 1):
                answer.append(num)
                answer.append(index+1)

        return answer