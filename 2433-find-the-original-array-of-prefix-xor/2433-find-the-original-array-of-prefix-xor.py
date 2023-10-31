class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer = [pref[0]]
        length = len(pref)
        
        for index in range(1, length):
            answer.append(pref[index - 1] ^ pref[index])
            
        return answer
        