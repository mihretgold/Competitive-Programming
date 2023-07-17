class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lengthHay = len(haystack)
        lengthNeedle = len(needle)
        ans = -1
        start = 0

        for end in range(lengthNeedle-1, lengthHay):
            if haystack[start:end+1] == needle:
                ans = start
                break

            start += 1

        return ans