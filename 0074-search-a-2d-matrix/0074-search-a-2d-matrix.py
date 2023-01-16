class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length_row = len(matrix)
        top = 0
        bottom = length_row - 1
        found = -1
        
        mid = (bottom + top)//2
        #Binary search to find the row
        while top <= bottom:
            
            print(matrix[mid][0])
            if matrix[mid][0] <= target:
                if matrix[mid][-1] >= target:
                    found = mid
                    break
                else:
                    top = mid + 1
            else:
                bottom = mid - 1
           
            mid = (bottom + top)//2
 
               
        if found == -1:
            return False
        #Binary search for the elements in the found row
        length_col = len(matrix[0])
        top_element = 0
        bottom_element = length_col - 1
        check = False        
        
        while top_element <= bottom_element:
            mid_element = (bottom_element + top_element)//2
            if matrix[found][mid_element] == target:
                check = True
                break
            elif matrix[found][mid_element] > target:
                bottom_element = mid_element - 1
            elif matrix[found][mid_element] < target:
                top_element = mid_element + 1
        
        return check
            
            