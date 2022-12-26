class Solution:
    def freqAlphabets(self, s: str) -> str:
        index = len(s) - 1  
        answer = ''
        while index >= 0:
            if s[index] == '#':
                answer = chr(96+int(s[index-2:index])) + answer
                index -= 3
                
            else: 
                answer = chr(96 + int(s[index])) + answer
                index -= 1
        return answer