class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        graph = {0: [1,3],1:[0,2,4], 2:[1, 5], 3: [0, 4], 4: [3, 5,1],5: [2,4]}
        target = '123450'
        gridList = "".join(str(num) for row in board for num in row)
        queue = deque()
        initial = 0
        for i in range(len(gridList)):
            if gridList[i] == '0':
                initial = i
                break
        
            
        queue.append((initial, gridList))
        move = 0
        visited = set()
        visited.add(gridList)


        while queue:
            length = len(queue)
            print(queue)
            for _ in range(length):
                current, gridList = queue.popleft()
                print(current, gridList)


                if gridList == target:
                    return move

                for child in graph[current]:
                    newGrid = list( gridList)
                    newGrid[child], newGrid[current] = newGrid[current], newGrid[child]
                    newGrid = ''.join(newGrid)
                    if newGrid not in visited:
                        queue.append((child, newGrid))
                        visited.add(newGrid)

            move += 1

        return -1