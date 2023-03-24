# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        arr = [0 for _ in range(1002)]
        count = 0
        sums = 0
        def calcPathSum(root, arr, l):
            nonlocal count
            if not root:
                return 

            arr[l] = root.val
            # if root.val == targetSum:
            #     count += 1
            
            
            i = 0
            while i < l+1:
                if sum(arr[i:l+1]) == targetSum:
                    count += 1
                i += 1
            
            
            calcPathSum(root.left, arr, l+1)
            calcPathSum(root.right, arr, l+1)

            return  
        
        calcPathSum(root, arr, 0)
        return count