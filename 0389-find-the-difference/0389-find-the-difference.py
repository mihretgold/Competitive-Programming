class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        word1 = Counter(s)
        word2 = Counter(t)
        
        for letter in word2:
            if word2[letter] != word1[letter]:
                return letter
            
            
            