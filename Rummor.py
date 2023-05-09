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
    arr = IL()
    graph = defaultdict(list)
    for _ in range(m):
        a, b = II()
        graph[a].append(b)
        graph[b].append(a)
 
    visted = set()
    answer = 0
    for num in graph:
        if num not in visted:
            queue = deque([num])
            visted.add(num)
            mini = arr[num-1]
 
            while queue:
                val = queue.popleft()
 
                for child in graph[val]:
                    if child not in visted:
                        visted.add(child)
                        queue.append(child)
                        mini = min(mini, arr[child-1])
 
            answer += mini
 
    for index in range(n):
        if index + 1 not in visted:
            answer += arr[index]
 
    print(answer)
 
 
 
T = 1
for ___ in range(T):
    solve()