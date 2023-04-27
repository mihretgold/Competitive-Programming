# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        answer = []
        while queue:
            length = len(queue)
            sums = 0
            for _ in range(length):
                node = queue.popleft()
                sums += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            answer.append(sums/length)

        return answer