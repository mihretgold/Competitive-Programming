# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def calc(root):
            if not root:
                return 
            
            calc(root.left)
            answer.append(root.val)
            calc(root.right)
            
        calc(root)
        return answer
        