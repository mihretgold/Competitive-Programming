# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        inorderVal = []

        if not root:
            return []

        inorderVal.extend(self.inorder(root.left))
        inorderVal.append(root.val)
        inorderVal.extend(self.inorder(root.right))        
            
        return inorderVal

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorderVal = self.inorder(root)
        return inorderVal[k-1]