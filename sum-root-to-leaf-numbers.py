# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sums = 0
        def calcSum(root, string):
            nonlocal sums
            if not root.right and not root.left:
                sums += int(string)

            if root.left:    
                calcSum(root.left, string + str(root.left.val))
            if root.right:
                calcSum(root.right, string + str(root.right.val))

        calcSum(root, str(root.val))
        return sums