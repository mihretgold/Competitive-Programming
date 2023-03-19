# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelDict = defaultdict(list)
        def calcTraversal(root, row, col):
            if not root:
                return

            levelDict[col].append([row, root.val])
            calcTraversal(root.left,row+1, col - 1)
            calcTraversal(root.right,row+1, col + 1)

        calcTraversal(root, 0, 0)
        sorting = list(levelDict.keys())
        sorting.sort()
        answer = []
        for num in sorting:
            temp = sorted(levelDict[num])
            tempArr = []
            for a, b in temp:
                tempArr.append(b)
            answer.append(tempArr)
        return answer