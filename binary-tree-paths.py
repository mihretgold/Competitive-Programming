# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        def leaf(root, path):
            if root and not root.left and not root.right:
                answer.append(path)
            if not root:
                return
            if root.right:
                leaf(root.right, path + "->"+ str(root.right.val))
            if root.left:
                leaf(root.left, path + "->"+ str(root.left.val))             
                
                

        leaf(root, str(root.val))
        return answer