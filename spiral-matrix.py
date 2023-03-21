class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        answer = []
        while True:
            for i in range(left, right+1):
                answer.append(matrix[top][i])
            if bottom == top:
                break
            top += 1
            for i in range(top, bottom+1):
                answer.append(matrix[i][right])
            if left == right:
                break
            right -= 1
            for i in range(right, left-1, -1):
                answer.append(matrix[bottom][i])
            if bottom == top:
                break
            bottom -= 1
            for i in range(bottom, top-1, -1):
                answer.append(matrix[i][left])
            if left == right:
                break
            left += 1

        return answer