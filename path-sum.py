# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        ans = False
        if not root:
            return ans

        def calcSum(root, currSum):
            nonlocal ans
            if ans == False:
                if not root.left and not root.right:
                    currSum += root.val
                    if currSum == targetSum:
                        ans = True
                        return
                    
                if ans:
                    return 
                
                if root.left:
                    left = calcSum(root.left, currSum + root.val)

                if root.right:
                    right = calcSum(root.right, currSum + root.val)
                
                return 
        
        calcSum(root, 0)
        return ans