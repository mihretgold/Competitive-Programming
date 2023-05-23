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

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        length = len(source)
        rep = {i:i for i in range(length)}
        count = [1]*length
        dicts = defaultdict(lambda : defaultdict(int))
        result = 0 
        sourceSet = set(source)

        for start, end in allowedSwaps:
            self.union(rep, count, start, end)

        for index in range(length):
            parent = self.find(rep, index)
            dicts[parent][source[index]] += 1
        

        for index in range(length):
            parent = self.find(rep, index) 
            if dicts[parent][target[index]]:
                dicts[parent][target[index]] -= 1
                result += 1

        result = length - result   
            

        return result