class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0]*n
        graph = defaultdict(list)
        check = [set()]*n
        queue =deque()
        visted = set()

        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()

            for child in graph[node]:
                indegree[child] -= 1
                check[child] = check[child].union(check[node])
                check[child].add(node)
                if indegree[child] == 0:
                    queue.append(child)
        for index in range(n):
            check[index] = sorted(check[index])

        return check