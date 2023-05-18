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
            if rep_x < rep_y:
                rep[rep_y] = rep_x
            else:
                rep[rep_x] = rep_y

    def connected(self,rep, x, y):
        return self.find(rep,x) == self.find(rep,y)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        length = len(s1)
        rep = {chr(i): chr(i) for i in range(ord('a'), ord('a') + 26)}
        count = {chr(i): 1 for i in range(ord('a'), ord('a') + 26)}
       
        answer = []
        for index in range(length):
            self.union(rep, count, s1[index], s2[index])

        for letter in baseStr:
            answer += self.find(rep, letter)

        return "".join(answer)