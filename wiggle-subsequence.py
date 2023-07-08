class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        up = (1, length - 1)
        down = (1, length - 1)

        for index in range(length - 2, -1, -1):
            temp_up = (0, 0)
            temp_down = (0, 0)
            if nums[index] < nums[up[1]] and up[0] + 1 >= down[0]:
                if up[0] + 1 == down[0] and  nums[index] < nums[down[1]]:
                    temp_down = (down[0], index)
                elif up[0] + 1 > down[0]:
                    temp_down = (up[0] + 1, index)
               
                    
            if nums[index] > nums[down[1]] and down[0] + 1 >= up[0]:
                if down[0] + 1 == up[0] and nums[index] > nums[up[1]]:
                    temp_up = (up[0], index)
                elif down[0] + 1 > up[0]:
                    temp_up = (down[0] + 1, index)

               
            
            if temp_up > temp_down or (temp_up == temp_down and temp_up[0] != 0):
                up = temp_up
            if temp_down > temp_up or (temp_up == temp_down and temp_up[0] != 0):
                down = temp_down

        result = max(up[0], down[0])
        return result