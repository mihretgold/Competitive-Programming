# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        store = defaultdict(int)
        
        def searchAvg(root, search):
            if not root:
                return 0
            
            left = searchAvg(root.left, search)
            right = searchAvg(root.right, search)
            
            answer = left + right
            if root.val == search:
                answer += 1
                
            return answer
        
        def calc(root):
            if not root:
                return (0, 0, 0)
            
            
            left = calc(root.left)
            right = calc(root.right)
            nodes = left[1] + right[1] + 1
            total = left[0] + right[0] + root.val
            avg = total // nodes
            answer = left[2] + right[2]
            if avg == root.val:
                answer += 1
                
            return (total, nodes, answer)
        
        
        
        
        
        return calc(root)[2]
        