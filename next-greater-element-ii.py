class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        greater = [-1 for _ in range(length)]
        stack = []
        
        for index in range(length):
            while stack and nums[stack[-1]] < nums[index]:
                greater[stack[-1]] = nums[index]
                stack.pop()
            stack.append(index)

        for index in range(length):
           while stack and index < stack[-1] and nums[stack[-1]] < nums[index]:
                greater[stack[-1]] = nums[index]
                stack.pop() 

        return greater