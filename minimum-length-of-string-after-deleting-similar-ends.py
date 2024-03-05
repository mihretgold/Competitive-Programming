class Solution:
    # remove similar later from ends
    # if end == start end ++, start ++ 
    # if != but == to prev start++ or end +=
    # else break 
    # return end - start + 1
    def minimumLength(self, s: str) -> int:
        start = 0
        length = len(s) 
        end = length - 1

        while start <= end:
            if s[start] == s[end] and start != end:
                start += 1
                end -= 1
            elif start >= 1 and s[start] == s[start - 1]:
                start += 1
            elif end < length - 1 and s[end] == s[end + 1]:
                end -= 1
            else:
                break

        return end - start + 1