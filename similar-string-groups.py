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

    def numSimilarGroups(self, strs: List[str]) -> int:
        length = len(strs)
        rep = {i: i for i in range(length)}
        count = {i: 1 for i in range(length)}

        for index in range(length):
            for idx in range(index + 1, length):
                difference = 0
                for i in range(len(strs[index])):
                    if strs[index][i] != strs[idx][i]:
                        difference += 1

                if difference <= 2:
                    self.union(rep, count, index, idx)

        answer = set()
        for index in range(length):
            self.find(rep, index)

        for key, val in rep.items():
            answer.add(val)

        return len(answer)