# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heightStore = defaultdict(int)

        def calc(root, height):
            if not root:
                return height - 1

            left = calc(root.left, height + 1)
            right = calc(root.right, height + 1)

            heightStore[root.val] = (max(left, right), height)
            return heightStore[root.val][0]

        calc(root, 0)
        queue = deque([root])
        level = 0
        answer = defaultdict(int)
       
        while queue:
            length = len(queue)
            maxx = -1
            store = []

            for _ in range(length):
                node = queue.popleft()
                
                if node.left:
                    store.append((heightStore[node.left.val][0], heightStore[node.left.val][1], node.left.val))
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    store.append((heightStore[node.right.val][0], heightStore[node.right.val][1], node.right.val))

            store.sort()
            for score, height, val in store:
                maxx = height - 1
                if store[-1][2] != val:
                    maxx = max(maxx, heightStore[store[-1][2]][0])
                elif len(store) > 1 and store[-2][2] != val:
                    maxx = max(maxx, heightStore[store[-2][2]][0])
                
                answer[val] = maxx       

        result = []
        for num in queries:
            result.append(answer[num])


        return result