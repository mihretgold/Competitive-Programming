class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        lengthR = len(img)
        lenCol = len(img[0])
        
        answer = [[0 for _ in range(lenCol)] for _ in range(lengthR)]
        def inbound(row, col):
            return (0 <= row < len(img)) and (0 <= col < len(img[0]))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        
        for row in range(lengthR):
            for col in range(lenCol):
                validPoints = 1
                total = img[row][col]
                for new_row, new_col in directions:
                    new_row += row
                    new_col += col
                    
                    if inbound(new_row, new_col):
                        validPoints += 1
                        total += img[new_row][new_col]
                        
                answer[row][col] = total//validPoints
        
        return answer
                    
                    