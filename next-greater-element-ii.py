class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        greater = [-1 for _ in range(length)]
        stack = []
        
        for index in range(2*length):
            while stack and nums[stack[-1]] < nums[index%length]:
                greater[stack[-1]] = nums[index%length]
                stack.pop() 
            stack.append(index%length)

    
           
        return greater