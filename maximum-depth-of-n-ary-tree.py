"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        result = 0

        def dfs(node):
            if not root:
                return 0
            if node.children == None:
                return 1           

            result = 0
            for child in node.children:
                result = max(result, dfs(child))
            return result + 1


        return dfs(root)