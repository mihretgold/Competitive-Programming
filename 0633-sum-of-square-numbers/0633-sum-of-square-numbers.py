class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = []
        for index in range(c+1):
            if index ** 2 <= c:
                nums.append(index ** 2)
            else:
                break
                
        length = len(nums)
        start = 0 
        end = length - 1
        answer = False
        while start <= end:
            result = nums[start] + nums[end] 
            if result == c:
                answer = True
                break
            elif result > c:
                end -= 1
            else:
                start += 1
        
        return answer