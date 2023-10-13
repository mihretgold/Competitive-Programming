class Solution:
    def longestPrefix(self, s: str) -> str:
        length = len(s)
        lsp = [0] * length
        answer = ""
        maxx = 0

        prevLsp, i = 0, 1

        while i < length:
            if s[i] == s[prevLsp]:
                prevLsp += 1
                lsp[i] = prevLsp
                i += 1

            elif prevLsp == 0:
                lsp[i] = 0
                i += 1
            else:
                prevLsp = lsp[prevLsp - 1]
        
        answer = s[length - lsp[-1] :]

        return answer