class Solution:
       def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return("")
        if len(strs) == 1:
            return(strs[0])
        
        prefix = strs[0]
        length = len(prefix)
        
        for letter in strs[1:]:
            #When we find non common char we remove it from prefix
            while prefix != letter[0:length]:
                prefix = prefix[0:(length -1)]
                length -= 1
                
                if length == 0:
                    return("")
        return(prefix)
                 
               
                        