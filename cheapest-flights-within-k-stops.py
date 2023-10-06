class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def dijkstra(start):
            distance = {node : float('inf') for node in range(n)}
            distance[start] = 0

            visted = set()
            heap = deque([(0, 0, start)])

            while heap:
                curr_weight,  dist, node = heap.popleft()
                if dist > k:
                    continue
                

                for child, weight in graph[node].items():
                    newdistance = curr_weight + weight
                    if newdistance < distance[child]:
                        distance[child] = newdistance
                        heap.append((newdistance,  dist + 1, child))

                

            return distance

        graph = defaultdict(lambda : defaultdict(int))

        for start, end, weight in flights:
            graph[start][end] = weight

        answer = dijkstra(src)

        
        return answer[dst] if answer[dst] != float('inf') else -1