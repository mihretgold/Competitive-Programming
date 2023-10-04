import math
import sys


def I(): return int(input())


def II(): return map(int, sys.stdin.readline().rstrip().split())


def IL(): return list(map(int, input().split()))


def SIL(): return sorted(map(int, input().split()))


def RSIL(): return sorted(map(int, input().split()), reverse=True)


from collections import defaultdict
from collections import Counter
from collections import deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, _heapify_max, nlargest, nsmallest
import copy


# sys.setrecursionlimit(2500)


def solve():
    n, m = II()
    graph = []
    distance = [0 for _ in range(n)]
    relaxants = [float('inf') for _ in range(n)]

    for _ in range(m):
        start, end, weight = II()
        graph.append((start-1, end-1, weight))



    for iter in range(n-1):
        for start, end, weight in graph:
            # print(start, end, weight)
            if distance[start] != float('inf') and distance[start] + weight < distance[end]:
                distance[end] = distance[start] + weight
                relaxants[end] = start

    lastRelaxed = -1
    for start, end, weight in graph:
        if distance[start] != float('inf') and distance[start] + weight < distance[end]:
            lastRelaxed = end


    if lastRelaxed == -1:
        print("NO")
    else:
        path = []
        visted = set()

        while True:
            if lastRelaxed == float('inf'):
                path.append(1)
                break

            path.append(lastRelaxed + 1)
            if lastRelaxed in visted:
                break

            visted.add(lastRelaxed)
            lastRelaxed = relaxants[lastRelaxed]

        print("YES")
        print(*path[::-1])




T = 1
for ___ in range(T):
    solve()