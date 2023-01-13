class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rowLength = len(mat[0])
        colLength = len(mat)
        answer = []
        j = 0
        count = 0
        while j < rowLength:
            temp = j
            i = 0
            tempList = []
            while i < colLength and j >= 0:
                if count % 2 != 0:
                    answer.append(mat[i][j])
                    i += 1
                    j -= 1
                else:
                    tempList.append(mat[i][j])
                    i += 1
                    j -= 1
            lengthTemp = len(tempList)
            tempList.reverse()
            for num in tempList:
                answer.append(num)
                
            j = temp + 1
            count += 1
        
        i = 1
        while i < colLength:
            temp_i = i
            j = rowLength - 1
            tempLowList = []
            while i < colLength and j >= 0:
                if count % 2 != 0:
                    answer.append(mat[i][j])
                    i += 1
                    j -= 1
                else:
                    tempLowList.append(mat[i][j])
                    i += 1 
                    j -= 1
            lengthTemp = len(tempLowList)
            tempLowList.reverse()
            for num in tempLowList:
                answer.append(num)
                
            i = temp_i + 1
            count += 1
            
        return answer