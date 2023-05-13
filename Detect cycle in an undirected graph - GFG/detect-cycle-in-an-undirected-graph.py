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
	           
	            


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends