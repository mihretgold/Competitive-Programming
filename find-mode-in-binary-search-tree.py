# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def countFrequency(root):
            nonlocal count
            if not root:
                return

            count[root.val] += 1           
            countFrequency(root.left)
            countFrequency(root.right)
        countFrequency(root)
        answer = []
        result = []
        
        for num in count:
            temp = [count[num], num]
            answer.append(temp)
        answer.sort(reverse = True)
        maxi = answer[0][0]
        for counts, num in answer:
            if counts == maxi:
                result.append(num)
            else:
                break
        return result