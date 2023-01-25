class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0 
        end = len(height) - 1
        maxi = 0
        while start < end:
            if height[start] < height[end]:
                width = end - start
                area = height[start] * width
                start += 1
            else:
                width = end - start
                area = height[end] * width
                end -= 1
            maxi = max(maxi, area)
                
        return maxi