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

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        rep = {i : i for i in range(n)}
        count = {i : 1 for i in range(n)}
        store = defaultdict(list)
        self.union(rep, count, 0, firstPerson)

        for x, y, time in meetings:
            store[time].append([x, y])

        store = OrderedDict(sorted(store.items()))
        length = len(meetings)
        
        for time in store:
            for x, y in store[time]:
                self.union(rep, count, x, y)

            for x, y in store[time]:
                if self.find(rep, x) != 0:
                    rep[x] = x
                if self.find(rep, y) != 0:
                    rep[y] = y

        answer = []

        for key, val in rep.items():
            if val == 0:
                answer.append(key)

    
        

        return answer