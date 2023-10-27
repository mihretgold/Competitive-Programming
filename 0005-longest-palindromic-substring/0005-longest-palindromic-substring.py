class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        maxx = ""
        LSP = [0] * length

        prevLSP, i = 0, 1

        while i < length:
            if s[i] == s[prevLSP]:
                prevLSP += 1
                LSP[i] = prevLSP 
                i += 1
            elif prevLSP == 0:
                LSP[i] = 0
                i += 1
            else:
                prevLSP = LSP[prevLSP - 1]
        
        
        
        for index in range(length):
            idx = 0
            j = index
            prefix = ""
            suffix = ""
            while idx <= j:
                if s[idx] == s[j]:
                    if idx != j:
                        suffix = s[j] + suffix
                    prefix += s[idx]
                    j -= 1
                elif LSP[index] <= LSP[idx] and s[idx] == s[index]:
                    idx += 1
                    continue
                else:
                    prefix = ""
                    suffix = ""
                    j = index                    
                idx += 1
                
            string = prefix + suffix
            if len(string) > len(maxx):
                maxx = string
                
        return maxx