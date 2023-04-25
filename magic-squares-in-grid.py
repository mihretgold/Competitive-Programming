class Solution:
    def numMagicSquaresInside(self, matrix: List[List[int]]) -> int:
        length_row = len(matrix)
        length_col = len(matrix[0])
        answer = 0
        magic_nums = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}

        if length_row < 3 or length_col < 3:
            return 0

        magic_grid = True
        for row in range(length_row-2):
            for col in range(length_col-2):
                check = 0
                sum_r1 = sum(matrix[row][col:col+3])
                sum_r2 = sum(matrix[row+1][col:col+3])
                sum_r3 = sum(matrix[row+2][col:col+3])
                if sum_r1 == sum_r1 == sum_r1:
                    check = 1
                else:
                    magic_grid = False

                sum_d1 = matrix[row][col] + matrix[row + 1][col + 1] + matrix[row + 2][col + 2]
                sum_d2 = matrix[row][col+2] + matrix[row + 1][col + 1] + matrix[row + 2][col]
                if sum_d1 != sum_d2:
                    magic_grid = False

                count = 0
                sums = 0
                check = defaultdict(int)
                for i in range(col, col + 3):
                    temp = 0
                    for j in range(row, row + 3):
                        check[matrix[j][i]] += 1
                        if count == 0:
                            sums += matrix[j][i]
                        else:
                            temp += matrix[j][i]
                    if temp != sums and count == 1:
                        magic_grid = False
                        break
                    count = 1
                
                if sums == sum_d1 == sum_r1 and  magic_grid == True and check == magic_nums:
                    magic_grid = True
                else:
                    magic_grid = False

                answer += magic_grid
                magic_grid = True

                        
        return answer