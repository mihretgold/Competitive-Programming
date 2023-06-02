# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mem = defaultdict(int)
    def rob(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        if root in self.mem:
            return self.mem[root]

        sum1 = 0
        sum2 = 0
        if root.left:
            leftRob = self.rob(root.left.left)
            rightRob = self.rob(root.left.right)
            sum1 = leftRob + rightRob

        if root.right:
            leftStill = self.rob(root.right.left)
            rightStill = self.rob(root.right.right)
            sum2 = leftStill + rightStill

        left = self.rob(root.left)
        right = self.rob(root.right)
        sum3 = left + right
        self.mem[root] = max(sum1 + sum2 + root.val, sum3)

        return self.mem[root]