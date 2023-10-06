class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        def dijkstra(start):
            distance = { node: -1 for node in range(n)}
            distance[start] = 0
            visted = set()

            heap = [(-1, start)]

            while heap:
                curr_weight, node = heappop(heap)

                if node in visted:
                    continue

                visted.add(node)

                for child, weight in graph[node].items():
                    new_distance = abs(curr_weight) * weight
                    if new_distance > distance[child]:
                        distance[child] = new_distance
                        heappush(heap, (-new_distance, child))

            return distance

        graph = defaultdict(lambda : defaultdict(int))

        length = len(edges)
        for index in range(length):
            start, end = edges[index]
            graph[start][end] = succProb[index]
            graph[end][start] = succProb[index]

        distance = dijkstra(start_node)
        return distance[end_node] if distance[end_node] != -1 else 0