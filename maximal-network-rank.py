class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        maxi = 0
        
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        for a, b in roads:
            length = (len(graph[a]) + len(graph[b])) - 1
            maxi = max(maxi, length)

        for i in range(n):
            for j in range(n):
                if i not in graph[j] and j not in graph[i] and i != j:
                    length = len(graph[i]) + len(graph[j])
                    maxi = max(maxi, length)

        return maxi