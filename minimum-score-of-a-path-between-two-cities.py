class Solution:
    def find(self,rep,  x):
        root = x
        while root != rep[root]:
            rep[root] = rep[rep[root]]
            root = rep[root]
        
        while x != root:
            rep[x], x = root, rep[x]           
            
        return root

    def union(self,rep, count,distance, x, y, d):
        rep_x = self.find(rep, x)
        rep_y = self.find(rep, y)

        if rep_x != rep_y:
            if count[rep_x] > count[rep_y]:
                distance[rep_x] = min(distance[rep_x], distance[rep_y], d)
                rep[rep_y] = rep_x
                count[rep_x] += count[rep_y]
            else:
                distance[rep_y] = min(distance[rep_y],distance[rep_x], d)
                rep[rep_x] = rep_y
                count[rep_y] += count[rep_x]
        else:
            distance[rep_y] = min(distance[rep_y], d)

    def connected(self,rep, x, y):
        return self.find(rep,x) == self.find(rep,y)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = {i : i for i in range(1, n+1)}
        count =  {i : 1 for i in range(1, n+1)}
        distance = {i : float('inf') for i in range(1, n+1)}

        for start, end, d in roads:
            self.union(rep, count, distance, start, end, d)

        answer = self.find(rep, 1)

        return distance[answer]