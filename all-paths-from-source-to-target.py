class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        def dfs(index, path):
            if index == len(graph)-1:
                result.append(path[:])
                return

            for neighbour in graph[index]:
                path.append(neighbour)
                dfs(neighbour, path[:])
                path.pop()
                                   

        dfs(0, [0])

        return result