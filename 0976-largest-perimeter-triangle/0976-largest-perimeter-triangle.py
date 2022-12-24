class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        first = 0
        second = 1 
        third = 2
        perimeter = 0
        length = len(nums)
        
        while(length > 2):
            if nums[first] < nums[second] + nums[third]:
                perimeter = nums[first] + nums[second] + nums[third]
                return perimeter
            first += 1
            second += 1
            third += 1
            length -= 1
        
        return 0
            
        