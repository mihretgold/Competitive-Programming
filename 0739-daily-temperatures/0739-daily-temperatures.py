class Solution:
    '''
    Algo
    1) start from back append index 0 last element to stack
    2) if next element is greater pop until it's not 
    3) put the last top element index - now index in list
    4) then push index of element to stack
    
    dict = {(73, 1) 74,}
    stack = [6, 2]
    [0, 0, 1,1,2,4,1,1 ]
    stack = [8, 7, 6]
    ''' 
    
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = []
        length = len(temperatures)
        
        for index in range(length-1, -1, -1):               
            while len(stack) > 0 and temperatures[index] >= temperatures[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                warmer = stack[-1] - index
                answer.append(warmer)
            else:
                answer.append(0)
            stack.append(index)
        answer.reverse()
            
        return answer
            
            