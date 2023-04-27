class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        # length_row = len(grid)
        # length_col = len(grid[0])

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        queue = deque()
        if grid[0][0] == 0:
            queue.append((0, 0))
        count = 0
        
        found = -1
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                if row == len(grid)-1 and col == len(grid)-1:
                    found = 0
                    break

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 1

            count += 1
            if found == 0:
                break

        if found == -1:
            count = -1

        return count