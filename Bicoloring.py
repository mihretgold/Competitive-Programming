import math
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter

def solve():
    nodes = I()
    while nodes != 0:
        edges = I()
        graph = defaultdict(list)
        visted = defaultdict(int)
        for index in range(edges):
            a, b = II()
            graph[a].append(b)
            graph[b].append(a)


        def dfs(vertex, color):
            visted[vertex] = color
            for neighbour in graph[vertex]:
                if neighbour not in visted:
                    if not dfs(neighbour, -color):
                        return False
                elif visted[vertex] == visted[neighbour]:
                    return False

            return True

        answer = True
        for num in graph:
            if num not in visted:
                answer = answer and dfs(num, 1)

        if answer:
            print("BICOLOURABLE.")
        else:
            print("NOT BICOLOURABLE.")
        nodes = I()


T = 1
for ___ in range(T):
    solve()
