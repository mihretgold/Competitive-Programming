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

    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        length = len(nums)
        segment = [0]*length
        rep = { i:i for i in range(length)}
        count = { i:1 for i in range(length)}
        sums = nums[:]
        answer = [0]*length
        maxi = 0

        def find(x):
            root = x
            while root != rep[root]:
                rep[root] = rep[rep[root]]
                root = rep[root]
            
            while x != root:
                rep[x], x = root, rep[x]           
                
            return root

        def union(x, y):
            rep_x = self.find(rep, x)
            rep_y = self.find(rep, y)

            if rep_x != rep_y:
                if count[rep_x] > count[rep_y]:
                    rep[rep_y] = rep_x
                    sums[rep_x] += sums[rep_y]
                    count[rep_x] += count[rep_y]
                else:
                    rep[rep_x] = rep_y
                    sums[rep_y] += sums[rep_x]
                    count[rep_y] += count[rep_x]
        

        for i in range(length - 1, -1, -1):
            answer[i] = maxi
            index = removeQueries[i]
            segment[index] = nums[index]
            if index - 1 >= 0 and segment[index-1] != 0:
                union(index, index - 1)

            if index + 1 < length and segment[index+1] != 0:
                union(index, index + 1)

            parent = find(index)
            maxi = max(maxi, sums[parent], segment[index])


        return answer