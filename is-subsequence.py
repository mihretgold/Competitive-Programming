class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        haystack = 0
        needle = 0
        lengthS = len(s)
        lengthT = len(t)

        while haystack < lengthT and needle < lengthS:
            if s[needle] == t[haystack]:
                needle += 1
                haystack += 1
            else:
                haystack += 1


        result = (needle == lengthS)

        return result