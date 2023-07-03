class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        numbers = defaultdict(tuple)
        index = defaultdict(int)
        length = len(board)
        alternate = True
        count = 1

        def inbound(row, col):
            return (0 <= row < len(board)) and (0 <= col < len(board))

        for i in range(length-1, -1, -1):
            if alternate:
                for j in range(length):
                    numbers[count] = (i, j)
                    index[(i,j)] = count
                    count += 1
                alternate = not alternate
            else:
                for j in range(length-1, -1, -1):
                    numbers[count] = (i, j)
                    index[(i,j)] = count
                    count += 1
                alternate = not alternate

        queue = deque([(length-1, 0)])
        moves = 0
        visted = set()

        while queue:
            lengthq = len(queue)
           
            for _ in range(lengthq):
                row, col = queue.popleft()
                

                if index[(row, col)] == length**2:
                    return moves

                num = index[(row, col)]
                for i in range(1, 7):
                    if (num+i) in numbers:
                        newR, newC = numbers[num+i]
                        
                        if board[newR][newC] != -1:
                            newR, newC = numbers[board[newR][newC]]

                        if (newR, newC) not in visted:
                            queue.append((newR, newC))
                            visted.add((newR, newC))

            moves += 1


        return -1