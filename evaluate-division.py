class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        store = defaultdict(lambda: defaultdict(float))
        length = len(equations)
        answer = []

        for index in range(length):
            top, bottom = equations[index]
            store[top][bottom] = values[index]
            store[bottom][top] = 1 / values[index]

        def bfs(start, target, product):
            if start not in store:
                return -1

            queue = deque([(start, 1)])
            visted = set()
            visted.add(start)

            while queue:
                node, product = queue.popleft()
                if node == target:
                    return product

                for child, value in store[node].items():
                    if child not in visted:
                        queue.append((child, product * value))
                        visted.add(child)

            return -1

        for start, end in queries:
            result = bfs(start, end, 1)
            answer.append(result)

        return answer