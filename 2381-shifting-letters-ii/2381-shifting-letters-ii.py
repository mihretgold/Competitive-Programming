class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        prefix = [0 for _ in range(length)]
        
        for start, end, shift in shifts:
            if shift == 0:
                shift = -1
            
            prefix[start] += shift
            if end+1 < length:
                prefix[end+1] -= shift
                       
        for index in range(1, length):
            prefix[index] += prefix[index-1]
        
        for index in range(length):
            prefix[index] %= 26
            
            
        ans = ""
        for index in range(length):
            check = ord(s[index]) + prefix[index]
            if check > 122:
                check -= 26
                
            ans += chr(check)
       
        return ans
        