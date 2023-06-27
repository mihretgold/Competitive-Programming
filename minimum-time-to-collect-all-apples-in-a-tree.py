class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)


        def dfs(node, parent):
            total_time = 0
            child_time = 0

            for child in graph[node]:
                if child == parent:
                    continue

                child_time = dfs(child, node)
                if(child_time or hasApple[child]):
                    total_time += child_time + 2

            return total_time

        return dfs(0, -1)