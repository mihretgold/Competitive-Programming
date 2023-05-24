# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque()
        visted = set()      

        def buildGraph(root):
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                buildGraph(root.right)

            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                buildGraph(root.left)

        buildGraph(root)
        answer = []
        count = 0
        
        queue.append(target.val)
        visted.add(target.val)
        # print(graph)

        while queue:
            length = len(queue)
            
            temp = []
            for _ in range(length):
                node = queue.popleft()
                temp.append(node)

                for child in graph[node]:
                    if child not in visted:
                        queue.append(child)
                        visted.add(child)

            answer = temp
            count += 1
            if count == k+1:
                break
        if count != k+1:
            answer = []
        return answer