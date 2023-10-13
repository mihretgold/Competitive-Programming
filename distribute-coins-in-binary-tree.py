# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        answer = 0
        if not root:
            return 0
        def calc(root):
            nonlocal answer
            if not root:
                return 0

            left = calc(root.left)
            right = calc(root.right)

            result = left + right + root.val - 1
            answer += abs(result)

            return result
        calc(root)
        return answer