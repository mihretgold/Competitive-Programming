import math
import sys
 
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
from collections import deque
sys.setrecursionlimit(2500)
 
 
def solve():
    n, m, p = II()
    grid = []
    for i in range(n):
        temp = list(input())
        grid.append(temp)
    found = [0, 0]
    moves = IL()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "M":
                found = [i, j]
                break
 
    def inbound(row, col):
        return (0 <= row < n) and (0 <= col < m)
    for num in moves:
        if num == 1:
            if inbound(found[0] - 1, found[1]) and grid[found[0]-1][found[1]] != "#":
                found[0] -= 1
        elif num == 2:
            if inbound(found[0] + 1, found[1]) and grid[found[0]+1][found[1]] != "#":
                found[0] += 1
        elif num == 3:
            if inbound(found[0], found[1] - 1) and grid[found[0]][found[1]-1] != "#":
                found[1] -= 1
        elif num == 4:
            if inbound(found[0], found[1] + 1) and grid[found[0]][found[1] + 1] != "#":
                found[1] += 1
 
    queue = deque([found])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = 0
    visted = set(found)
    count = 0
    while queue:
        length = len(queue)
        for _ in range(length):
            row, col = queue.popleft()
 
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and (new_row, new_col) not in visted and grid[new_row][new_col] != "#":
                    answer += 1
                    queue.append((new_row, new_col))
                    visted.add((new_row, new_col))
        count += 1
        if count == p:
            break
 
    print(answer)
 
T = 1
for ___ in range(T):
    solve()