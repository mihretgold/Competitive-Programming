class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0]*n
        graph = defaultdict(list)
        maxi = 0

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            indegree[start] += 1
            indegree[end] += 1

        queue = deque()
        for index in range(n):
            if indegree[index] <= 1:
                queue.append(index)

        answer = []
        while queue:
            length = len(queue)
            temp = []
            for _ in range(length):
                node = queue.popleft()
                temp.append(node)

                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        queue.append(child)
            
            answer = temp

        return answer