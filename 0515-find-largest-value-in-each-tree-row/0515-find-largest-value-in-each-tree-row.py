# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        graph = defaultdict(set)
        
        def traversal(root, parent):
            if not root:
                return 
            if parent != -1:
                graph[root].add(parent)
                graph[parent].add(root)
            
            left = traversal(root.left, root)
            right = traversal(root.right, root)
            
        traversal(root, -1)
        
        queue = deque([(root, -1)])
        answer = []
        visted = set()
        visted.add(root)
        
        while queue:
            length = len(queue)
            
            maxx = float('-inf')
            # print(queue)
            for _ in range(length):
                node, parent = queue.popleft() 
                maxx = max(maxx, node.val)
                
                
                for child in graph[node]:
                    if (parent == -1 or child != parent) and child not in visted:
                        queue.append((child, node))
                        visted.add(child)
                       
                        # print(node, child)
            answer.append(maxx)  
            # print(answer)
            
        
        return answer
            
            
        