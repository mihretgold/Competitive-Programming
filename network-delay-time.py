class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(start):
            distance = { node: float('inf') for node in range(1, n + 1)}
            distance[start] = 0
            visted = set()

            heap = [(0, start)]

            while heap:
                curr_weight, node = heappop(heap)

                if node in visted:
                    continue

                visted.add(node)

                for child, weight in graph[node].items():
                    new_distance = curr_weight + weight
                    if new_distance < distance[child]:
                        distance[child] = new_distance
                        heappush(heap, (new_distance, child))

            return max(distance.values())

        graph = defaultdict(lambda: defaultdict(int))

        for start, target, weight in times:
            graph[start][target] = weight

        answer = dijkstra(k)

        return answer if answer != float('inf') else -1