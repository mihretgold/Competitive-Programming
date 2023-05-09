import math
import sys
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
from collections import deque
from heapq import heapify ,heappop , heappush,heappushpop,heapreplace,_heapify_max ,nlargest ,nsmallest
 
sys.setrecursionlimit(2500)
 
 
def solve():
    n, m = II()
    matrix = []
    visted = set()
    for _ in range(n):
        a = list(input())
        # colors= colors.union(set(a))
        matrix.append(a)
 
 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
    def inbound(row, col):
        return (0 <= row < n) and (0 <= col < m)
 
    def bfs(row, col, pr, pc, color):
        queue = deque([(row, col, pr, pc, color)])
        visted.add((row, col))
        while queue:
            row, col, pr, pc, color = queue.popleft()
 
 
            for r, c in directions:
                r += row
                c += col
 
                if inbound(r, c) and (r, c) != (pr, pc) and matrix[r][c] == color:
                    if (r, c) in visted:
                        return True
                    elif (r, c) not in visted:
                        visted.add((r, c))
                        queue.append((r, c, row, col, color))
 
 
 
        return False
 
    for row in range(n):
        for col in range(m):
            if (row, col) not in visted and bfs(row, col, -1, -1, matrix[row][col]):
                print("Yes")
                sys.exit()
    else:
        print("No")
 
 
 
 
T = 1
for ___ in range(T):
    solve()