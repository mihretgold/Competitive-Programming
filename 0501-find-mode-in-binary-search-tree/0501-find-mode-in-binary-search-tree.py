# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        store = defaultdict(int)
        def calc(root):
            if not root:
                return 
            
            store[root.val] += 1
            calc(root.left)
            calc(root.right)
            
        calc(root)
        answer = []
        
        maxx = 0
        for _, count in store.items():
            maxx = max(maxx, count)
            
        for num, count in store.items():
            if count == maxx:
                answer.append(num)
                
        return answer