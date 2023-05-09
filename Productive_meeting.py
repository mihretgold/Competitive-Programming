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
    n = I()
    a = IL()
    heap = []
    answer = []
    for i in range(n):
        heappush(heap, (-a[i], i+1))
 
 
    while len(heap) > 1:
        maxi, length = heappop(heap)
        num, index = heappop(heap)
        if maxi != 0 and num != 0:
            answer.append([index, length])
            if maxi+1 != 0:
                heappush(heap, (maxi+1, length))
            if num+1 != 0:
                heappush(heap, (num+1, index))
 
 
    print(len(answer))
    for i in range(len(answer)):
        print(*answer[i])
 
T = I()
for ___ in range(T):
    solve()