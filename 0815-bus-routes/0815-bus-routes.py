class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        if source == target:
            return 0
        
        for bus in range(len(routes)):
            length = len(routes[bus])
            for index in range(length):
                graph[routes[bus][index]].append(bus)
                
        visted = set()
        queue = deque()
        for val in graph[source]:
            visted.add(val)
            queue.extend(routes[val])
      
        level = 1
        while queue:
            length = len(queue)
            
            for _ in range(length):
                bus = queue.popleft()
                
                if bus == target:
                    return level
                for child in graph[bus]:     
                    if child not in visted:
                        queue.extend(routes[child])
                        visted.add(child)
                        
            level += 1
            
        return -1