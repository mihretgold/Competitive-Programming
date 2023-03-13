# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        BST = False
        def inorder(root):
            InorderVal = []
            if root:
                InorderVal.extend(inorder(root.left))
                InorderVal.append(root.val)
                InorderVal.extend(inorder(root.right))
            else:
                return []
            return InorderVal
        answer = inorder(root)
        check = answer[:]
        check.sort()
        duplicate = set(check)
        if check == answer and len(duplicate) == len(check):
            BST = True

        return BST