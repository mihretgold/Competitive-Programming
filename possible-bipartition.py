class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for start, end in dislikes:
            graph[start].append(end)
            graph[end].append(start)

        length = len(dislikes)
        visted = defaultdict(int)

        def dfs(vertex, color):
            stack = [(vertex, color)]

            while stack:
                vertex, color = stack.pop()

                for child in graph[vertex]:
                    if child not in visted:
                        visted[child] = -color
                        stack.append((child, -color))
                    elif visted[child] == visted[vertex]:
                        return False

            return True

        for vertex in graph:
            if vertex not in visted:
                if not dfs(vertex, 1):
                    return False

        return True