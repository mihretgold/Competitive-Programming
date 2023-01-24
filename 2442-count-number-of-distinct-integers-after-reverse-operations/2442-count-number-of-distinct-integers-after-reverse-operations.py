class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reverse = []
        length_nums = len(nums)
        for index in range(length_nums):
            list_num = []
            for num in str(nums[index]):
                list_num.append(num)            
            list_num.reverse()
            rev = int("".join(list_num))
            nums.append(rev)
        
        answer = len(set(nums))
        
        return answer