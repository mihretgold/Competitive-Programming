class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        length = len(heights)
        maxi = 0
        preiviousSmaller = [0 for _ in range(length)]
        nextSmaller = [(length-1) for _ in range(length)]

        for index in range(length):
            while stack and heights[stack[-1]] > heights[index]:
                nextSmaller[stack.pop()] = index - 1

            if stack:
                preiviousSmaller[index] = stack[-1] + 1

            stack.append(index)


        for index in range(length):
            width = (nextSmaller[index] - preiviousSmaller[index]) + 1
            area = heights[index]*width
            maxi = max(maxi, area)



        return maxi
        
        
        