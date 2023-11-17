class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[] for _ in range(numRows)]

        answer[0].append(1)

        for row in range(1, numRows):
            for col in range(row + 1):
                left = 0
                right = 0

                if row - 1 >= 0:
                    if col - 1 >= 0 and col - 1 <= row - 1:
                        left = answer[row - 1][col - 1] 
                    if col >= 0 and  col <= row - 1:
                        right = answer[row - 1][col]

                answer[row].append(left + right)

        return answer
