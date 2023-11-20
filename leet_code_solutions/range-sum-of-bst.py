# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def calc(root):
            if not root:
                return 0

            left = calc(root.left)
            right = calc(root.right)

            answer = left + right
            if low <= root.val <= high:
                return answer + root.val
            else:
                return answer

        return calc(root)
        