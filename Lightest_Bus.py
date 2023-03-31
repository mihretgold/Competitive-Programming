def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter

def solve():
    n = I()
    a = IL()
    prefix = []
    prefix.append(sum(a[:12]))
    for index in range(12, n, 6):
        if index + 6 < n:
            prefix.append(sum(a[index:index+6]))
        else:
            prefix.append(sum(a[index:]))

    mini = min(prefix[0], prefix[-1])
    for i in range(1, len(prefix)):
        weight = prefix[i] + prefix[i-1]
        mini = min(mini, weight)

    print(mini)


T = I()
for ___ in range(T):
    solve()
