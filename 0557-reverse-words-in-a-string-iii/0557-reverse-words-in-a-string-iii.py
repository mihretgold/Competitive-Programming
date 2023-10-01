class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        answer = ""
        
        for string in words:
            answer += string[::-1] + " "
            
        return answer[:-1]
        