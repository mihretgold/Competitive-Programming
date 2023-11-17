# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def calc(root, leftOrRight):
            if not root:
                return 0

            if not root.right and not root.left:
                if leftOrRight == 1:
                    return root.val
                else:
                    return 0

            answer = 0
            answer += calc(root.left, 1)
            answer += calc(root.right, 0)

            return answer

        return calc(root, -1)