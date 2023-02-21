class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        for row in range(0, n, 3):
            for col in range(0, m, 3):
                validate = set()
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        if board[i][j] != "." and board[i][j] in validate:
                            return False
                        elif board[i][j] != ".":
                            validate.add(board[i][j])
                            
        for i in range(n):
            validate_row = set()
            for j in range(m):
                if board[i][j] != "." and board[i][j] in validate_row:
                    return False
                elif board[i][j] != ".":
                    validate_row.add(board[i][j])
                            
        for i in range(n):
            validate_col = set()
            for j in range(m):
                if board[j][i] != "." and board[j][i] in validate_col:
                    return False
                elif board[j][i] != ".":
                    validate_col.add(board[j][i])
                        
                            
        return True
        
        