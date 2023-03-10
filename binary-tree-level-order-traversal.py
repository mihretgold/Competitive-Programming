# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelDict = defaultdict(list)
        def calcLevel(root, h):
            if not root:
                return 
            
            levelDict[h].append(root.val)
            calcLevel(root.left, h+1)
            calcLevel(root.right, h+1)
        calcLevel(root, 0)
        return list(levelDict.values())