class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        stack = []
        length = len(height)
        for index in range(length):
            while stack and height[stack[-1]] <= height[index]:
                popped = height[stack[-1]]
                stack.pop()
                if len(stack) >= 1:
                    heightRect = min(height[stack[-1]], height[index]) - popped
                    width = (index - stack[-1]) - 1
                    area = heightRect*width
                    count += area

            stack.append(index)

        return count