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

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        length = len(s)
        rep = {i : i for i in range(length)}
        count = {i : 1 for i in range(length)}
        swaps = defaultdict(lambda : defaultdict(int))
        
        for a, b in pairs:
            self.union(rep, count, a, b)

        for index in range(length):
            parent = self.find(rep, index)
            swaps[parent][s[index]] += 1

        answer = ""
        for index in range(length):
            parent = self.find(rep, index)
            val = min(swaps[parent])
            swaps[parent][val] -= 1
            if swaps[parent][val] == 0:
                swaps[parent].pop(val)
            answer += val


        return answer