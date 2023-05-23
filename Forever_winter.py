import functools
import math
import sys
from functools import cmp_to_key
 
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
from collections import deque
sys.setrecursionlimit(2500)
from heapq import heapify ,heappop , heappush,heappushpop,heapreplace,_heapify_max ,nlargest ,nsmallest
 
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
 
 
def connected(rep, x, y):
    return find(rep, x) == find(rep, y)
 
def solve():
    n, m = II()
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for i in range(m):
        a, b = II()
        graph[a].append(b)
        graph[b].append(a)
        indegree[a] += 1
        indegree[b] += 1
 
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] <= 1:
            queue.append(i)
    count = 0
    answer = []
    while queue:
        length = len(queue)
        for _ in range(length):
            node = queue.popleft()
            count += 1
 
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 1:
                    queue.append(child)
        answer.append(count)
        count = 0
 
    print(answer[1], int(answer[0]/answer[1]))
 
 
 
 
T = I()
for ___ in range(T):
    solve()