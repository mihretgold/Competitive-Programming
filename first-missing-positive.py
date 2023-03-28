class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        answer = 1
        index = 0
        
        while index < length:
            correct_position = nums[index] - 1
            if correct_position >= 0 and correct_position <= (length-1) and nums[index] != nums[correct_position]:
                nums[index], nums[correct_position] = nums[correct_position], nums[index]
            else:
                index += 1


        i = 1
        for index in range(length):
            if nums[index] != i:
                break
            i += 1

        return i