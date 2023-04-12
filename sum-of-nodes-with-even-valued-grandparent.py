# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sums = 0
        def evenGrandParent(root):
            nonlocal sums
            if root:
                if root.val % 2 == 0:
                    if root.left:
                        if root.left.left:
                            sums += root.left.left.val
                        if root.left.right:
                            sums += root.left.right.val
                    if root.right:
                        if root.right.left:
                            sums += root.right.left.val
                        if root.right.right:
                            sums += root.right.right.val
                evenGrandParent(root.left)
                evenGrandParent(root.right)

        evenGrandParent(root)
        return sums