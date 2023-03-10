# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelDict = defaultdict(list)
        def checkWidth(root, level):
            if not root:
                return 

            if root.right:
                root.right.val = 2*root.val+1
            if root.left:
                root.left.val = 2*root.val

            levelDict[level].append(root.val)
            checkWidth(root.left, level+1)
            checkWidth(root.right, level+1)

        root.val = 1
        checkWidth(root, 0)
        maxi = -1
        for level in levelDict.values():
            temp = (level[-1] - level[0]) + 1
            maxi = max(maxi, temp)

        return maxi