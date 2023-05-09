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
    n = I()
    arr = []
    for _ in range(2):
        string = input()
        arr.append(list(string))
 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    def inbound(row, col):
        return (0 <= row < 2) and (0 <= col < n)
 
    queue = deque([(0, 0)])
    visted = set()
    visted.add((0, 0))
    found = 0
    while queue:
        row, col = queue.popleft()
 
        if row == 1 and col == n-1:
            print("YES")
            found = 1
            break
 
 
        for r_c, c_c in directions:
            n_r = row + r_c
            n_c = col + c_c
 
            if inbound(n_r, n_c) and (n_r, n_c) not in visted and arr[n_r][n_c] == "0":
                queue.append((n_r, n_c))
                visted.add((n_r, n_c))
 
 
    if found == 0:
        print("NO")
 
 
 
T = I()
for ___ in range(T):
    solve()