# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleteSet = set(to_delete)
        answer = []

        def traversal(root):
            if not root:
                return 0


            left = traversal(root.left)
            right = traversal(root.right)


            if left:
                root.left = None

            if right:
                root.right = None

            if root.val in deleteSet:
                if root.left:
                    answer.append(root.left)
                if root.right:
                    answer.append(root.right)
                return 1

            return 0

        traversal(root)
        
        if root and root.val not in deleteSet:
            answer.append(root)

        return answer