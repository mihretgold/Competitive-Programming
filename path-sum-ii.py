# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        if not root:
            return answer
        
        def calc(root, path, total):
            if total == targetSum and not root.left and not root.right:
                answer.append(path)
                return 

            if not root:
                return
            if root.left:
                calc(root.left, path + [root.left.val], total + root.left.val)
            if root.right:
                calc(root.right, path + [root.right.val], total + root.right.val)

        calc(root, [root.val], root.val)

        return answer