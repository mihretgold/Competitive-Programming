class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        colors = [0]*length
        answer = []
        
        def dfs(node):
            stack = [node]
            
            while stack:
                node = stack.pop()
                if colors[node] == 1:
                    return False
                
                colors[node] = 1
                for child in graph[node]:
                    if colors[child] == 2:
                        continue
                    if not dfs(child):
                        return False
                    stack.append(child)

                colors[node] = 2
            return True

        for num in range(length):
            if dfs(num):
                answer.append(num)

        return answer