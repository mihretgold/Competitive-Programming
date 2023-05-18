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

    def removeStones(self, stones: List[List[int]]) -> int:
        rep = defaultdict(tuple)
        count = defaultdict(tuple)
        length = len(stones)
        parents = set()

        for a, b in stones:
            rep[(a, b)] = (a, b)
            count[(a, b)] = 1

        for row in range(length):
            for col in range(length):
                if stones[row][0] == stones[col][0] or stones[row][1] == stones[col][1]:
                    self.union(rep, count, tuple(stones[row]), tuple(stones[col]))

        for a, b in stones:
            val = self.find(rep, (a, b))
            parents.add(val)

        result = length - len(parents)
        return result