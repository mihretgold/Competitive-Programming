import math
import sys
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
def RSIL(): return sorted(map(int, input().split()), reverse=True)
from collections import defaultdict
from collections import Counter
from collections import deque
from heapq import heapify ,heappop , heappush,heappushpop,heapreplace,_heapify_max ,nlargest ,nsmallest
import copy
import math

sys.setrecursionlimit(2500)

def solve():
    n =I()
    matrix = []
    count = 0
    for _ in range(n):
        row = list(map(int, input()))
        matrix.append(row)

    for row in range(math.ceil(n/2)):
        for col in range(n//2):
            total = sum([
                matrix[row][col],
                matrix[col][-1 - row],
                matrix[-1 - row][-1 - col],
                matrix[-1 - col][row],
            ])

            count += min(total, 4 - total)


    print(count)




T = I()
for ___ in range(T):
    solve()
