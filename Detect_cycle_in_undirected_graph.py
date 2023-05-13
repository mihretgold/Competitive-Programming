from typing import List
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        length = len(adj)
       
        visted  = set()
                
                
       
        def bfs(node, parent): 
            queue = deque([(node, parent)])
            
            while queue:
                node , parent = queue.popleft()
               
                for child in adj[node]:
                    if child in visted and child != parent:
                        return True
                       
                    if child not in visted:
                        queue.append((child, node))
                        visted.add(child)
                       
            return False
            
        for index in range(length):
            if index not in visted:
                visted.add(index)
                if bfs(index, -1):
                    return True
                    
            
        return False
               
                
