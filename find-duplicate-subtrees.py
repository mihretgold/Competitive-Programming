# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        answer = []
        store = defaultdict(int)

        def calc(root):
            if not root:
                return ""
                
            left = calc(root.left)
            right = calc(root.right)

            subtree = left + "," + right + "," + str(root.val)
            store[subtree] += 1
            if store[subtree] == 2:
                answer.append(root)


            return subtree
        calc(root)
        return answer