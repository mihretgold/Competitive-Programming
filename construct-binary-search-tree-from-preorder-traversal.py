# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:      
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        check = preorder[0]
        if len(preorder) == 1:
            return root

        length = len(preorder)
        i = 1
        while i < length:
            if preorder[i] < check:
                i += 1
            else:
                break
        # print(i)
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])

        return root