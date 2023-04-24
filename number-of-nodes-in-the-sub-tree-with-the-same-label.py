class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:    
        answer = [0 for _ in range(n)]
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            count = collections.Counter()

            for child in graph[node]:
                if child != parent:
                   count += dfs(child, node)

            count[labels[node]] += 1
            answer[node] += count[labels[node]]
            return count



        dfs(0, -1)

        return answer