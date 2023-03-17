# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightVal = defaultdict(list)
        def rightSide(root, level):
            if not root:
               return 
            
            rightVal[level].append(root.val)
            rightSide(root.left, level+1)
            rightSide(root.right, level+1)

        rightSide(root, 0)
        answer = []
        for num in rightVal:
            answer.append(rightVal[num][-1])           

        return answer