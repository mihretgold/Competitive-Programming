import math
import random
import sys
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
 
sys.setrecursionlimit(2500)
 
 
def solve():
    n = I()
    a = SIL()
    answer = a[-1]
    for index in range(n - 1):
        answer = answer & a[index]
 
    print(answer)
 
 
 
 
 
 
T = I()
for ___ in range(T):
    solve()
 