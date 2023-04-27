class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        length_row = len(mat)
        length_col = len(mat[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(mat)) and (0 <= col < len(mat[0]))


        queue = deque()
        visted = set()
        
        for row in range(length_row):
            for col in range(length_col):
                if mat[row][col] == 0:
                    queue.append((row, col))

        count = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                mat[row][col] = count

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if inbound(new_row, new_col) and (new_row, new_col) not in visted and mat[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        visted.add((new_row, new_col))

            count += 1


        return mat