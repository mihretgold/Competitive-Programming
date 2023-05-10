class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [0]*numCourses
        graph = defaultdict(list)
        check = True

        for to, froms in prerequisites:
            graph[froms].append(to)

        def dfs(node):
            if color[node] == 1:
                return False

            if color[node] == 2:
                return True
            color[node] = 1

            for child in graph[node]:
                if not dfs(child):
                    return False

            color[node] = 2
            return True

        for index in range(numCourses):
            if not dfs(index):
                check = False
                break


        return check