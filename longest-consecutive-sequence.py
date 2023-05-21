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

    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        rep = defaultdict(int)
        count = defaultdict(int)
        nums = set(nums)
        parents = defaultdict(int)
        result = 0

        for num in nums:
            rep[num] = num
            count[num] = 1

        for num in nums:
            if num + 1 in nums:
                self.union(rep, count, num, num+1)
            if num - 1 in nums:
                self.union(rep, count, num, num-1)
        
        for num in nums:
            parent = self.find(rep, num)
            parents[parent] += 1

        if parents: 
            result = max(parents.values())
        
        return result