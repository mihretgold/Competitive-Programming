import math
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter

def solve():
    n = I()
    matrix = []
    path = 0
    for _ in range(n):
        nums = IL()
        for j in range(n):
            path += nums[j]

    print(path//2)





T = 1
for ___ in range(T):
    solve()