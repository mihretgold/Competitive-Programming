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

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        if length == 0:
            return 0
        edges = []
        res = 0
        rep = defaultdict(tuple)
        count = defaultdict(int)

        for index in range(length):
            val = tuple(points[index])
            rep[val] = val
            count[val] = 1
            for i in range(length-1):
                if index != i:                
                    x = abs(points[index][0] - points[i][0])
                    y = abs(points[index][1] - points[i][1])
                    d = x + y
                    edges.append((d, val, tuple(points[i])))
                    
        edges.sort()
        for dis, start, end in edges:
            if not self.connected(rep, start, end):
                res += dis
                self.union(rep, count, start, end)

        return res









        