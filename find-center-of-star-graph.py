class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)

        for a, b in edges:
            graph[a] += 1
            graph[b] += 1

        maxi = 0
        answer = 0
        for num in graph:
            if graph[num] > maxi:
                maxi = graph[num]
                answer = num

        return answer