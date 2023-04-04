class Solution:
    def calcGCD(self, a:int, b:int)-> int:
        if a == 0:
            return b
        if b == 0:
            return a
        
        return self.calcGCD(b, a%b)

    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return self.calcGCD(nums[-1], nums[0])