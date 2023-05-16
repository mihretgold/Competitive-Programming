class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        check = [set()]*numCourses
        length = len(queries)
        result = [False]*length

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()
        for index in range(numCourses):
            if indegree[index] == 0:
                queue.append(index)

        while queue:
            node = queue.popleft()

            for child in graph[node]:
                indegree[child] -= 1
                check[child] = check[child].union(check[node])
                check[child].add(node)
                if indegree[child] == 0:
                    queue.append(child)
        
        
        for i in range(length):
            a, b = queries[i]
            if b in check[a]:
                result[i] = True
                
        return result