class Solution:
    '''
    0: 1, 2, 7 
    1: 3, 6, 7
    q = []
    q = [, 7]
    '''
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        lengthRow = len(routes)
        buses = defaultdict(list)

        for row in range(lengthRow):
            lengthCol = len(routes[row])
            for col in range(lengthCol):
                buses[routes[row][col]].append(row)

        if buses[source] and source == target:
            return 0
            
        visted = set()
        start = []
        for index in buses[source]:
            visted.add(index)
            start.extend(routes[index])

        queue = deque(start)
        count = 1

        while queue:
            length = len(queue)

            for _ in range(length):
                vertex = queue.popleft()
                
                if vertex == target:
                    return count

                for child in buses[vertex]:
                    if child not in visted:
                        visted.add(child)
                        for route in routes[child]:
                            queue.append(route)
            
            count += 1

        return -1