class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       answer = 0
       length = len(nums)

       for i in range(1,length+1):
           answer ^= i

       for num in nums:
           answer ^= num

       return answer