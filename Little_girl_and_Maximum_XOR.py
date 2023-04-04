import math
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
def solve():
    l, r = II()
    num = l ^ r
    msb = len(bin(num)[2:])
    if num == 0:
        msb = 0
    answer = (2 ** msb) - 1
    print(answer)
 
 
 
T = 1
for ___ in range(T):
    solve()