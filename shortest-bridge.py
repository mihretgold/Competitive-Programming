class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        length_row = len(grid)
        length_col = len(grid[0])
        visted = set()

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        answer = []
        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()

                for row_change, col_change in directions:
                    row_change += row
                    col_change += col
                    if inbound(row_change, col_change) and (row_change, col_change) not in visted and grid[row_change][col_change] == 1:
                        queue.append((row_change, col_change))
                        visted.add((row_change, col_change))


        found = 0
        for row in range(length_row):
            for col in range(length_col):
                if grid[row][col] == 1:
                    visted.add((row, col))
                    bfs(row, col)
                    found = 1
                    break
            if found == 1:
                break

        queue = deque(visted)
        count = 0
        found = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()


                for row_change, col_change in directions:
                    row_change += row
                    col_change += col
                    if inbound(row_change, col_change) and (row_change, col_change) not in visted:
                        if grid[row_change][col_change] == 1:
                            found = 1
                            break
                        queue.append((row_change, col_change))
                        visted.add((row_change, col_change))
            if found == 1:
                break
            count += 1
            

        return count