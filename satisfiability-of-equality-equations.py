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

    def equationsPossible(self, equations: List[str]) -> bool:
        rep = { chr(i):chr(i) for i in range(ord('a'), ord('a') + 26)}
        count = { chr(i):1 for i in range(ord('a'), ord('a') + 26)}
        query = []

        for equation in equations:
            if equation[1] == "=":
                self.union(rep, count, equation[0], equation[3])
            else:
                query.append((equation[0], equation[3]))

        check = True
        for a, b in query:
            if self.connected(rep, a, b):
                check = False
                break


        return check