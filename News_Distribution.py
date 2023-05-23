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
 
 
def find(rep, x):
    root = x
    while root != rep[root]:
        rep[root] = rep[rep[root]]
        root = rep[root]
 
    while x != root:
        rep[x], x = root, rep[x]
 
    return root
 
 
def union(rep, count, x, y):
    rep_x = find(rep, x)
    rep_y = find(rep, y)
 
    if rep_x != rep_y:
        if count[rep_x] > count[rep_y]:
            rep[rep_y] = rep_x
            count[rep_x] += count[rep_y]
        else:
            rep[rep_x] = rep_y
            count[rep_y] += count[rep_x]
 
 
def connected(self, rep, x, y):
    return find(rep, x) == find(rep, y)
 
def solve():
    n, m = II()
    rep = {i : i for i in range(1, n+1)}
    count = {i : 1 for i in range(1, n+1)}
    dicts = defaultdict(int)
    answer = []
 
    for _ in range(m):
        a = IL()
        length = len(a)
        for i in range(1, length-1):
            union(rep,count,  a[i], a[i+1])
 
    for i in range(1, n+1):
        parent = find(rep, i)
        dicts[parent] += 1
 
    for i in range(1, n + 1):
        parent = find(rep, i)
        answer.append(dicts[parent])
 
    print(*answer)
 
 
 
T = 1
for ___ in range(T):
    solve()