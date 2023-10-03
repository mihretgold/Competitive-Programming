class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        store = defaultdict(int)
        tracePath = defaultdict(int)
        
        if edges == []:
            return sum(price) // 2
        def bfs(node, target):
            queue = deque([node])
            visted = set()
            visted.add(node)
            store[node] += 1
            level = 0
            while queue:
                length = len(queue)
                
                for _ in range(length):
                    node = queue.popleft()

                    if node == target:
                        return level

                    for child in graph[node]:
                        if child not in visted:
                            queue.append(child)
                            tracePath[child] = node
                            visted.add(child)
                            

                level += 1
            return 0

        
        @cache
        def dp(node, canHalf, parent):
            cost = price[node] * store[node]

            if canHalf:
                cost //= 2
        
            for child in graph[node]:
                if child != parent:
                    if not canHalf:
                        cost += min(dp(child, False, node),dp(child, True, node))
                    else:
                        cost += dp(child, False, node)
                    
            return cost

        queue = deque()

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        for start, target in trips:
            bfs(start, target)
            node = target
            while node != start:
                store[node] += 1
                node = tracePath[node]
            tracePath = defaultdict(int)

        mini = float('inf')
        for node in graph:         
            mini = min(mini, dp(node, False, -1), dp(node, True, -1))

        return mini