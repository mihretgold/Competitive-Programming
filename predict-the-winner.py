class Solution:
    '''
    if p1:
        right 
    '''
    def check(self, nums, l, r):
        if l == r:
            return nums[l]
        
        return max(nums[l] - self.check(nums, l+1, r),nums[r] - self.check(nums, l, r-1) )





    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)-1
        score = self.check(nums, 0,length)

        return score >= 0