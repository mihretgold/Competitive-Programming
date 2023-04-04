def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
def solve():
    n = I()
    a = IL()
    sets = set(a)
    for i in range(n):
        xors = 0
        for j in range(n):
            if j != i:
                xors ^= a[j]
 
        if xors in sets:
            print(a[i])
            break
 
 
T = I()
for ___ in range(T):
    solve()
