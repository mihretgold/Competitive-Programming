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
            count[rep_y] = 1
        else:
            rep[rep_x] = rep_y
            count[rep_y] += count[rep_x]
            count[rep_x] = 1
 
 
def connected(rep, x, y):
    return find(rep, x) == find(rep, y)
 
def solve():
    n, m = II()
    rep = {i : i for i in range(1, n+1)}
    count = {i : 1 for i in range(1, n+1)}
    free = 1
    def maxCount():
        maxi = 0
        arr = []
        for num in count:
            arr.append(count[num])
 
        arr.sort(reverse=True)
        for i in range(free):
            maxi += arr[i]
 
        return maxi
 
    for _ in range(m):
        a, b = II()
        if not connected(rep, a, b):
            union(rep, count, a, b)
        else:
            free += 1
        maxi = maxCount()
        print(maxi-1)
 
 
 
 
T = 1
for ___ in range(T):
    solve()