# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def calcAverage(root):
            nonlocal count
            if root and not root.right and not root.left:
                count += 1
                return [root.val, 1]
            if not root:
                return [0, 0]
            
           
            right = calcAverage(root.right)
            left = calcAverage(root.left)
            sums = right[0] + left[0] + root.val
            print(right, left)
            n = right[1] + left[1] + 1
            if sums//n == root.val:
                count += 1 
            return [sums, n]

        calcAverage(root)
        return count