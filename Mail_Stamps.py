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
    vist = set()
    for _ in range(n):
        a, b = map(int, input().split())
        vist.add(a)
        vist.add(b)
        graph[a].append(b)
        graph[b].append(a)
 
 
 
 
 
 
    def dfs(node, visted):
        stack = [node]
        check = [node]
 
 
        while stack:
            node = stack.pop()
            visted.add(node)
 
            for child in graph[node]:
                if child not in visted:
                    stack.append(child)
                    check.append(child)
 
            if len(check) == len(vist):
                return  check
        return []
    answer  = []
    for node in graph:
        if len(graph[node]) == 1:
            answer = dfs(node, set())
            break
 
    print(*answer)
 
 
 
 
 
 
 
T = 1
for ___ in range(T):
    solve()