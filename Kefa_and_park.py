import math
import sys
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
 
# sys.setrecursionlimit(3500)
 
 
def solve():
    n, m = II()
    arr = IL()
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = II()
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
 
 
 
    def dfs(current, parent, cats):
        nonlocal m
        stack = [(current, parent, cats)]
        answer = 0
 
        while stack:
            current, parent, cats = stack.pop()
            if cats > m:
                continue
            leaf = 1
            for child in tree[current]:
                if child != parent:
                    leaf = 0
                    stack.append((child, current, (cats * arr[child]) + arr[child]))
            answer += leaf
        return answer
 
    result = dfs(0, -1, arr[0])
 
    print(result)
 
 
T = 1
for ___ in range(T):
    solve()