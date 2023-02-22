class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        length = len(s)
        
        start = 0
        maxi = 0
        for end in range(length):
            if s[end] in check:
                while s[end] in check:
                    check.remove(s[start])
                    start += 1                
            check.add(s[end])
            maxi = max(maxi, end - start + 1)
                
        return maxi