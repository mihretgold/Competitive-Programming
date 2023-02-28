class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        stack_greater = []
        minimum =  [0 for _ in range(length)]

        for index in range(length):
            # Find minimum from previous nums
            if index == 0:
                minimum[index] = 0
            else:
                if nums[index] < nums[minimum[index-1]]:
                    minimum[index] = index
                else:
                    minimum[index] = minimum[index - 1]
            
            # Find previous greater
            while len(stack_greater) != 0 and nums[stack_greater[-1]] <= nums[index]:
                stack_greater.pop()
                
            if len(stack_greater) != 0:
                if nums[minimum[stack_greater[-1]]] < nums[index]:
                    return True
            stack_greater.append(index)
                
            
        return False