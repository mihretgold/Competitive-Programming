def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
def solve():
    num = I()
    count = 1
    i = num
    check = 1
    if num & 1 == 0:
        check = 2
 
    while i > check:
        string = bin(i)
        power = len(string) - 3
        i = i % (2**power)
        if i < check:
            break
        count += 1
    print(count)
 
 
T = 1
for ___ in range(T):
    solve()