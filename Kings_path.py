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
    x0, y0, x1, y1 = II()
    n = I()
    possible = defaultdict(list)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
 
    def inbound(row, col):
        return (0 <= row < 10**9) and (0 <= col < 10**9)
    for _ in range(n):
        a, b, c= II()
        possible[a].append((b, c))
 
    queue = deque([(x0, y0)])
    visted = set((x0, y0))
    count = 0
    found= 0
    while queue:
        length = len(queue)
        for _ in range(length):
            row , col = queue.popleft()
            if row == x1 and col == y1:
                found = 1
                break
 
            for r, c in directions:
                r += row
                c += col
                if inbound(r, c) and (r, c) not in visted:
                    for a, b in possible[r]:
                        if a <= c <= b:
                            queue.append((r, c))
                            visted.add((r, c))
 
                            break
        if found == 1:
            print(count)
            break
        count += 1
    if found == 0:
        print(-1)
 
 
 
 
T = 1
for ___ in range(T):
    solve()