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

    for i in range(n):
        nums = IL()
        arr = []
        for j in range(n):
            if nums[j] == 1:
                arr.append(j+1)
        print(len(arr), *arr)




T = 1
for ___ in range(T):
    solve()