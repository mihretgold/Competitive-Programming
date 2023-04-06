import math
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter

def solve():
    n = I()
    t = I()
    adjList = defaultdict(list)
    for i in range(t):
        a = list(map(int, input().split()))
        if a[0] == 1:
            adjList[a[1]].append(a[2])
            adjList[a[2]].append(a[1])
        else:
            print(*adjList[a[1]])





T = 1
for ___ in range(T):
    solve()