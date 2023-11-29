class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def calc(idx1, idx2):
            if idx1 == len(s) and idx2 == len(p):
                return True
            if idx1 == len(s):
                if p[idx2] == "*":
                    answer = calc(idx1, idx2 + 1)
                    return answer
                elif idx2 < len(p)- 1 and p[idx2 + 1] == "*":
                    answer = calc(idx1, idx2 + 2)
                    return answer
                else:
                    return False

            if idx2 == len(p):
                return False

            if p[idx2] != "." and p[idx2] != "*":
                if idx2 < len(p) - 1 and p[idx2 + 1] == "*":
                    if p[idx2] == s[idx1]:
                        answer = calc(idx1, idx2 + 2) or calc(idx1 + 1, idx2 + 1)
                    else:
                        answer = calc(idx1, idx2 + 2) 
                elif p[idx2] != s[idx1]:
                    return False
                else:
                    answer = calc(idx1 + 1, idx2 + 1)
            elif p[idx2] == ".":
                if idx2 < len(p) - 1 and p[idx2 + 1] == "*":
                    answer = calc(idx1, idx2 + 2) or calc(idx1 + 1, idx2 + 1)
                else:
                    answer = calc(idx1 + 1, idx2 + 1)
            else:
                if p[idx2 - 1] == "." or p[idx2 - 1] == s[idx1]:
                    left = calc(idx1 + 1, idx2)
                    right = calc(idx1 + 1, idx2 + 1)
                    same = calc(idx1, idx2 + 1)
                    answer = left or right or same
                else:
                    answer = calc(idx1, idx2 + 1)
                    

            return answer

        return calc(0, 0)
            