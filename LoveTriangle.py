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
    for index in range(n):
        check = a[a[index] - 1]
        if index + 1 == a[check - 1]:
            print("Yes")
            break
    else:
        print("NO")
 
 
T = 1
for ___ in range(T):
    solve()