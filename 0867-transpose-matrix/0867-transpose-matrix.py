class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        lengthRow = len(matrix)
        lengthCol = len(matrix[0])
        answer = []
        
        for i in range(lengthCol):
            temp = []
            for j in range(lengthRow):
                temp.append(matrix[j][i])
                
            answer.append(temp)
                
                
        return answer
        