class Solution:
       def longestCommonPrefix(self, strs: List[str]) -> str:
            #Sort list because the most common prifix can be checked from the first element and the last
            strs.sort()
            length = len(strs[0])
            right = 0
            left = len(strs) - 1
            answer = ''
            
            #Check letter on the first and last index of the list
            
            for index in range(length):
                if strs[right][index] == strs[left][index]:
                    answer += strs[right][index]
                else:
                    break
            
            return answer
                 
               
                        