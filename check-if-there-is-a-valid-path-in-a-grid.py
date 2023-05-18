class Solution:
    def find(self,rep,  x):
        root = x
        while root != rep[root]:
            rep[root] = rep[rep[root]]
            root = rep[root]
        
        while x != root:
            rep[x], x = root, rep[x]           
            
        return root

    def union(self,rep, count, x, y):
        rep_x = self.find(rep, x)
        rep_y = self.find(rep, y)

        if rep_x != rep_y:
            if count[rep_x] > count[rep_y]:
                rep[rep_y] = rep_x
                count[rep_x] += count[rep_y]
            else:
                rep[rep_x] = rep_y
                count[rep_y] += count[rep_x]

    def connected(self,rep, x, y):
        return self.find(rep,x) == self.find(rep,y)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions =  {1:(0, 1, 0, 1), 2:(1, 0, 1, 0), 3:(0, 0, 1, 1), 4:(0, 1, 1, 0), 5:(1, 0, 0, 1), 6:(1, 1, 0, 0)}
        length_row = len(grid)
        length_col = len(grid[0])
        rep = {(i, j) : (i, j) for i in range(length_row) for j in range(length_col)}
        count = {(i, j) : 1 for i in range(length_row) for j in range(length_col)}
      
        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        for row in range(length_row):
            for col in range(length_col):
                new_row = row + 1
                new_col = col + 1
                if inbound(new_row, col) and directions[grid[row][col]][2] and directions[grid[new_row][col]][0]:
                    self.union(rep,count, (row, col), (new_row, col))
                if inbound(row, new_col) and directions[grid[row][col]][1] and directions[grid[row][new_col]][3]:
                    self.union(rep,count, (row, col), (row, new_col))


        answer = self.connected(rep, (0, 0), (length_row-1, length_col-1))

        return answer