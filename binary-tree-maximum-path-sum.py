# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float(-inf)
        def calcMaxPathSum(root):
            nonlocal maxi
            if not root:
                return 0

            left = calcMaxPathSum(root.left)
            right = calcMaxPathSum(root.right)

            sums = root.val + left + right
            sum_left = root.val + left
            sum_right = root.val + right
            maxi = max(maxi, sums, root.val,sum_left, sum_right)
            val = max(root.val, root.val + max(left, right))
            return val   

        calcMaxPathSum(root)
        return maxi