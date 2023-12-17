class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = zip(*matrix)   
                
        return answer
        