import math
 
 
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
def solve():
    n = I()
    a = IL()
    count = 0
    msb = defaultdict(int)
    for index in range(n):
        string = bin(a[index])[2:]
        msb[len(string)] += 1
 
    for num in msb:
        if msb[num] > 1:
            count += (msb[num] - 1)/2 * (msb[num])
 
    print(int(count))
 
 
T = I()
for ___ in range(T):
    solve()