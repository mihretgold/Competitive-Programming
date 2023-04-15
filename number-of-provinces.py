class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visted = set()
        length_row = len(isConnected)
        length_col = len(isConnected[0])
        graph = defaultdict(list)
      
        for row in range(length_row):
            for col in range(length_col):
                if isConnected[row][col] == 1:
                    graph[row+1].append(col+1)

        def dfs(vertex):
            visted.add(vertex)
            if len(graph[vertex]) == 1:
                return

            for neighbour in graph[vertex]:
                if neighbour not in visted:
                    dfs(neighbour)

        answer = 0
        for vertex in graph:
            if vertex not in visted:
                dfs(vertex)
                answer += 1
        

        return answer