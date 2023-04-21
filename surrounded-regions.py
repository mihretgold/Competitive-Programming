class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        length_row = len(board)
        length_col = len(board[0])
        visted = set()
        flip = set()
        res = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(board)) and (0 <= col < len(board[0]))
        check = 0
        def dfs(row, col):
            visted.add((row, col))
            flip.add((row, col))
            nonlocal check
            if row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1:
                check = 1

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) and (new_row, new_col) not in visted and board[new_row][new_col] == "O":
                    dfs(new_row, new_col)
                    


        for row in range(length_row):
            for col in range(length_col):
                if (row, col) not in visted and board[row][col] == "O":
                    dfs(row, col)
                    if check == 1:
                        flip = set()
                        check = 0
                    res = res.union(flip)
        
        for row in range(length_row):
            for col in range(length_col):
                if (row,col) in res:
                    board[row][col] = "X"

        return board