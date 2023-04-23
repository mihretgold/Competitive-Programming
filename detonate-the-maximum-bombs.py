class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        length = len(bombs)
        graph = defaultdict(list)
        for bomb in range(length):
            x, y, r = bombs[bomb]
            for possible in range(bomb+1, length):
                i, j, rad = bombs[possible]
                incircle = (x - i)**2 + (y - j)**2
                outcircle = (i - x)**2 + (j - y)**2
                
                if incircle <= r**2:
                    graph[bomb].append(possible)
                elif bomb not in graph:
                    graph[bomb] = []
                
                if outcircle <= rad**2:
                    graph[possible].append(bomb)
                elif possible not in graph:
                    graph[possible] = []

        
        def dfs(vertex, visted):
            answer = 1            
            visted.add(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visted:
                    answer += dfs(neighbour, visted) 

            return answer

        maxi = 1

        for vertex in graph:
            answer = dfs(vertex, set())
            maxi = max(maxi, answer)


        return maxi