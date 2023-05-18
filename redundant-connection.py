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

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        length = len(edges)
        rep = {i : i for i in range(1, length+1)}
        count = {i : 1 for i in range(1, length+1)}

        for start, end in edges:            
            if self.connected(rep, start, end):
                return [start, end]
            else:
                self.union(rep, count, start, end)