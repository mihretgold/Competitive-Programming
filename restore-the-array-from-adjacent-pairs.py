class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        visted = set()
        answer = []
        def dfs(node):
            answer.append(node)
            
            for child in graph[node]:
                if child not in visted:
                    visted.add(child)
                    dfs(child)


        for num in graph:
            if len(graph[num]) == 1:
                visted.add(num)
                dfs(num)
                break

        return answer