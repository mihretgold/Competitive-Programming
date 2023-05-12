class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        length = len(quiet)
        graph = defaultdict(list)
        indegree = [0] * length

        for start, end in richer:
            graph[start].append(end)
            indegree[end] += 1

        queue = deque()
        answer = [i for i in range(length)]
        for index in range(length):
            if indegree[index] == 0:
                queue.append(index)

        while queue:
            node = queue.pop()

            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

                if quiet[answer[node]] < quiet[answer[child]]:
                    answer[child] = answer[node]
                

        return answer