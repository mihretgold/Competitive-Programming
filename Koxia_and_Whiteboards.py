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
    a = IL()
    b = IL()
    
    i = 0
    j = 0
    heapify(a)
    while j < m:
        heappop(a)
        heappush(a, b[j])
        j += 1
 
 
    print(sum(a))
 
T = I()
for ___ in range(T):
    solve()