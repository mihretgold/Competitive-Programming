# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def calc(root1, root2):
            if  root1 is root2:
                return True
            if not root1 or  not root2 or root1.val != root2.val:
                return False
            left = calc(root1.left, root2.left) or calc(root1.left, root2.right)
            right = calc(root1.right, root2.left) or calc(root1.right, root2.right)

            return left and right

        return calc(root1, root2)