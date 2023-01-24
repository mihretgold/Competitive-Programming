class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reverse = []
        length_nums = len(nums)
        for index in range(length_nums):
            string = str(nums[index])[::-1]
            rev = int(string)
            nums.append(rev)
        
        answer = len(set(nums))
        
        return answer