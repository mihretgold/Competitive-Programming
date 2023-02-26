class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack_first = []
        stack_second = []
        length = len(s)
        first = 0
        second = 0
        check1 = 'a'
        check2 = 'b'
        count = 0
        
        if y > x:
            first = y
            second = x
        else:
            first = x
            second = y
            check1 = 'b'
            check2 = 'a'            
        
        for index in range(length):
            if len(stack_first) != 0 and s[index] == check1 and stack_first[-1] == check2:
                count += first
                stack_first.pop()
            else:
                stack_first.append(s[index])
        
        size = len(stack_first)
        for index in range(size):
            if len(stack_second) != 0 and stack_first[index] == check2 and stack_second[-1] == check1:
                count += second
                stack_second.pop()
            else:                
                stack_second.append(stack_first[index])
            
        return count
            
            
                