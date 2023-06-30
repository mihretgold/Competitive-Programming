import functools
import math
import sys
from functools import cmp_to_key
 
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()), reverse= True)
from collections import defaultdict
from collections import Counter
from collections import deque
sys.setrecursionlimit(2500)
from heapq import heapify ,heappop , heappush,heappushpop,heapreplace,_heapify_max ,nlargest ,nsmallest
 
 
def solve():
    n = I()
    a = IL()
    setp = []
    setn = []
    setz = []
    count = 0
    for num in a:
        if num > 0:
            setp.append(num)
        elif num == 0:
            setz.append(num)
        else:
            count += 1
 
    countN = 0
    index = 0
    while index < n:
        if countN < 1 and a[index] < 0:
            setn.append(a[index])
            index += 1
            countN += 1
        elif not setp and a[index] < 0:
            while countN < 3 and index < n:
                setp.append(a[index])
                countN += 1
                index += 1
        elif a[index] < 0:
            setz.append(a[index])
            index += 1
            countN += 1
        else:
            index += 1
 
 
 
 
    print(len(setn), *setn)
    print(len(setp), *setp)
    print(len(setz), *setz)
 
 
 
T = 1
for ___ in range(T):
    solve()