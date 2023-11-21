class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        wordsS = defaultdict(str)
        wordsT = defaultdict(str)
        length = len(s)

        for index in range(length):
            if t[index] not in wordsT and s[index] not in wordsS:
                wordsT[t[index]] = s[index]
                wordsS[s[index]] = t[index]
            elif wordsT[t[index]] != s[index] or wordsS[s[index]] != t[index]:
                return False

        return True
            

        

