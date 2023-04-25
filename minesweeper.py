class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        visted = set()
        
        def inbound(row, col):
            return (0 <= row < len(board)) and (0 <= col < len(board[0]))


        

        def dfs(row, col, board):
            count = 0

            if board[row][col] == "M":
                board[row][col] = "X"
                return

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) and board[new_row][new_col] == "M":
                    count += 1
            if count > 0:
                board[row][col] = str(count)
                return

            board[row][col] = "B"
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col)  and board[new_row][new_col] == "E":
                        dfs(new_row, new_col, board)
            
           


        dfs(click[0], click[1], board)
        return board