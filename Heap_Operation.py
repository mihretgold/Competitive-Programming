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
from heapq import heapify ,heappop , heappush,heappushpop,heapreplace,_heapify_max ,nlargest ,nsmallest
 
 
 
def solve():
    n = I()
    records = []
    answer = []
    heap = []
    visted = set()
    for _ in range(n):
        a =  input().split()
        if a[0] == "insert":
            a[1] = int(a[1])
            heappush(heap, a[1])
            answer.append(["insert", a[1]])
 
        elif a[0] == "getMin":
            a[1]= int(a[1])
            while heap and heap[0] < a[1]:
                answer.append(["removeMin"])
                heappop(heap)
            if not heap or heap[0] > a[1]:
                answer.append(["insert", a[1]])
                heappush(heap, a[1])
            answer.append(["getMin", a[1]])
 
 
        else:
            if not heap:
                answer.append(["insert", "-1"])
                heappush(heap, "-1")
            heappop(heap)
            answer.append(["removeMin"])
    print(len(answer))
    for i in range(len(answer)):
        print(*answer[i])
 
T = 1
for ___ in range(T):
    solve()