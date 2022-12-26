class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        map_num={'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        answer1 = 0
        answer2 = 0
        for num in num1:
            answer1 = 10*answer1 + map_num[num]
        
        for num in num2:
            answer2 = 10*answer2 + map_num[num]
        
        result = answer1*answer2
        
        return str(result)