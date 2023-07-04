class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)

        for start, end in enumerate(parent):
            if end != -1:
                graph[end].append(start)

        res = 0
        

        def dfs(node):
            nonlocal res
            maxi = 0
            max2 = 0            
            
            for child in graph[node]:
                val = dfs(child) 
                if s[child] == s[node]:
                    continue
                if val > maxi:
                    max2 = maxi
                    maxi = val
                elif val > max2:
                    max2 = val

            
            res = max(res, maxi + max2 + 1)
            return maxi + 1

        
        dfs(0)
        return res