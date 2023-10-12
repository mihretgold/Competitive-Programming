class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        minScore = nums[0]
        length = len(nums)
        for index in range(1, length):
            minScore = minScore & nums[index]


        if minScore != 0:
            return 1

        
        answer = 0
        score = nums[0]
    

        for index in range(length):
            score = score & nums[index]
            if score == 0:
                answer += 1
                if index + 1 < length:
                    score = nums[index + 1]

               



        return answer