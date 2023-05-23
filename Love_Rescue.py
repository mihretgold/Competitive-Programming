
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
    n = I()
    Valya = input()
    Tolya = input()
    rep = {chr(i): chr(i) for i in range(ord('a'), ord('a')+26)}
    count = {chr(i): 1 for i in range(ord('a'), ord('a')+26)}
    answer = []
    for i in range(n):
        if not connected(rep, Valya[i], Tolya[i]):
            answer.append((Valya[i], Tolya[i]))
            union(rep,count, Valya[i], Tolya[i])
 
    print(len(answer))
    for i in range(len(answer)):
        print(answer[i][0], " ", answer[i][1])
 
 
 
 
T = 1
for ___ in range(T):
    solve()
