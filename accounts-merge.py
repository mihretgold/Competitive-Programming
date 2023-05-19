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

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rep = defaultdict(str)
        count = defaultdict(str)
        names = defaultdict(str)
        parents = defaultdict(set)
        answer = []

        for account in accounts:
            length = len(account)
            for index in range(1, length):
                rep[account[index]] = account[index]
                count[account[index]] = 1
                names[account[index]] = account[0]

        for account in accounts:
            length = len(account)
            for index in range(1, length-1):
                self.union(rep, count, account[index], account[index+1])

        for account in accounts:
            length = len(account)
            for index in range(1, length):
                parent = self.find(rep, account[index])
                parents[parent].add(account[index])

        for account in parents:
            temp = []
            name = names[account]
            temp.append(name)
            temp += sorted(parents[account])
            answer.append(temp)

        return answer