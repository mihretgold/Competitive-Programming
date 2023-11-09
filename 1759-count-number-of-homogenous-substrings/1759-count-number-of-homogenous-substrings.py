class Solution:
    def countHomogenous(self, s: str) -> int:
        answer = 0
        length = len(s)
        left = 0
        MOD = (10**9) + 7
        
        for end in range(length):
            diff = end - left + 1
            if end < length - 1 and s[left] != s[end + 1]:
                substrings = int(diff*(diff + 1)/2)
                answer += substrings
                left = end + 1
            elif end == length - 1:
                substrings = int((diff)*(diff + 1)/2)
                answer += substrings
                
                
        return answer % MOD
                
                