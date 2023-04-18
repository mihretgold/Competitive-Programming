class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visted = defaultdict(int)
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(vertex, color):
            visted[vertex] = color

            for neighbour in graph[vertex]:
                if neighbour not in visted:
                    if not dfs(neighbour, -color):
                        return False
                elif visted[neighbour] == visted[vertex]:
                    return False

            return True

        for node in graph:
            if node not in visted:
                if not dfs(node, 1):
                    return False

        return True