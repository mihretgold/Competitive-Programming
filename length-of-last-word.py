class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stringArray = s.split();
        length = len(stringArray[-1])


        return length