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

    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        rep = {i:i for i in range(n)}
        countU = {i:1 for i in range(n)}
        
        ans = []

        for person1, person2 in requests:
            parent1 = self.find(rep, person1)
            parent2 = self.find(rep, person2)
            found = 0

            for p1, p2 in restrictions:
                first = self.find(rep, p1)
                second = self.find(rep, p2)

                if parent1 == first and parent2 == second or parent1 == second and parent2 == first:
                    ans.append(False)
                    found = 1
                    break
            if not found:
                self.union(rep, countU, person1, person2)
                ans.append(True)

        return ans