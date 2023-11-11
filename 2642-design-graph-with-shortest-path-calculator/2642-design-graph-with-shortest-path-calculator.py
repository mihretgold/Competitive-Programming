class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.distance = {i: float('inf') for i in range(n)}
        self.graph = defaultdict(lambda: defaultdict(int))
        
        for start, end, cost in edges:
            self.graph[start][end] = cost
       
        
#         self.distance[0] = 1
#         heap = ((0, 0))
        
#         while heap:
#             node, cost = heappop(heap)
            
#             for child, pathCost in self.graph.items():
#                 newCost = cost + pathCost
#                 if newCost < self.distance[child]:
#                     self.distance[child] = newCost
#                     heappush(heap, (child, newCost))

    def calc(self, start):
        n = len(self.distance)
        self.distance = {i: float('inf') for i in range(n)}
        self.distance[start] = 0
        heap = [(start, 0)]
        
        while heap:
            node, cost = heappop(heap)
            
            for child, pathCost in self.graph[node].items():
                newCost = cost + pathCost
                # print(self.distance)
                if newCost < self.distance[child]:
                    self.distance[child] = newCost
                    heappush(heap, (child, newCost))
                    
        
        

    def addEdge(self, edge: List[int]) -> None:
        start, end, cost = edge
        self.graph[start][end] = cost        

    def shortestPath(self, node1: int, node2: int) -> int:
        self.calc(node1)
        answer = self.distance[node2] 
        return answer if answer != float('inf') else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)