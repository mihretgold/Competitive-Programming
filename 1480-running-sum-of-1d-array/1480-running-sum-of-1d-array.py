class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums =sum(nums)
        p = nums[0]
        length = len(nums)
        answer = []
        answer.append(p)
            
        for i in range(1, length):
            p += nums[i]
            ans = sums -(sums - p)
            answer.append(ans)
            
            
        return answer