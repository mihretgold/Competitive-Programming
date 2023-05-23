class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def inbound(row, col):
            return (0 <= row < len(maze)) and (0 <= col < len(maze[0]))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = deque([tuple(entrance)])
        visted = set()
        visted.add(tuple(entrance))

        count = 0
        found = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                if row == 0 or row == len(maze)-1 or col == 0 or col == len(maze[0])-1:
                    if row != entrance[0] or col != entrance[1]:
                        return count

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if inbound(new_row, new_col) and maze[new_row][new_col] == "." and (new_row, new_col) not in visted:
                        queue.append((new_row, new_col))
                        visted.add((new_row, new_col))

            count += 1

        return -1