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
        
        graph = defaultdict(lambda: float('-inf'))
        
        def traversal(root, length):
            if not root:
                return 
            if graph[length] < root.val:
                graph[length] = root.val
            
            left = traversal(root.left, length + 1)
            right = traversal(root.right, length + 1)
            
        traversal(root, 0)
        graph = OrderedDict(sorted(graph.items()))
        answer = list(graph.values())
       
        return answer
            
            
        