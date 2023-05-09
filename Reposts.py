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
    graph = defaultdict(list)
    for _ in range(n):
        post = list(input().split())
        graph[post[-1].lower()].append(post[0].lower())
        if post[0].lower() not in graph:
            graph[post[0].lower()] = []
 
    queue = deque(["polycarp"])
    count = 0
    while queue:
        length = len(queue)
        for _ in range(length):
            node = queue.popleft()
 
            for child in graph[node]:
                queue.append(child)
 
        count += 1
 
    print(count)
 
 
T = 1
for ___ in range(T):
    solve()