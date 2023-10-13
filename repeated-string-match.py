class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        length = len(b)
        lsp = [0] * length

        prevLsp, i = 0, 1

        while i < length:
            if b[i] == b[prevLsp]:
                prevLsp += 1
                lsp[i] = prevLsp
                i += 1

            elif prevLsp == 0:
                lsp[i] = 0
                i += 1
            else:
                prevLsp = lsp[prevLsp - 1]

        i, j = 0, 0
        answer = 0

        while i <= len(a):
            if i == len(a):
                answer += 1
                i = 0
            if a[i] == b[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
                if answer > 1:
                    return - 1
            else:
                if answer > 1:
                    return - 1
                j = lsp[j-1]


            if j == length:
                return answer + 1


        return -1