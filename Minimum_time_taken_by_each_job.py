from typing import List
from collections import defaultdict


from typing import List
from collections import deque


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        answer = ["0"]*n
        for start, end in edges:
            graph[start].append(end)
            indegree[end] += 1
            
        
        queue = deque()    
        for index in range(1, n+1):
            if indegree[index] == 0:
                queue.append(index)
             
        count = 1  
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                answer[node-1] = str(count)
                
                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)

            count += 1
            
        return " ".join(answer)