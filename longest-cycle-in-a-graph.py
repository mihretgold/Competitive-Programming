class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        length = len(edges)

        for index in range(length):
            if edges[index] != -1:
                graph[index].append(edges[index])
                indegree[edges[index]] += 1

        
        colors = [[0, 0] for _ in range(length)]
        maxi = -1
        def dfs(vertex, count):
            nonlocal maxi
            if colors[vertex][0] == 2:
                return 

            if colors[vertex][0] == 1:
                maxi = max(maxi, (count - colors[vertex][1]))
                return 

            colors[vertex][0] = 1
            colors[vertex][1] = count
            if vertex in graph:
                for child in graph[vertex]:
                    dfs(child, count + 1)

            colors[vertex][0] = 2

        for node in graph:
            if colors[node][0] == 0:
                dfs(node, 0) 
    
        return maxi