import math


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter


def solve():
    n, m = II()
    infected = SIL()
    uninfected = [(infected[0] - 1) + (n - infected[-1])]
    answer = 0
    for i in range(1, m):
        uninfected.append(infected[i]-infected[i-1]-1)

    uninfected.sort(reverse=True)

    if uninfected[0] > 1:
        answer += uninfected[0]-1
    else:
        answer += uninfected[0]

    infect = 2
    for infection in uninfected[1:]:
        infection -= infect * 2
        if infection > 0:
            infect += 1
            infection -= 1
            if infection > 1:
                infect += 1
                answer += infection
            else:
                answer += 1

        else:
            break

    print(n-answer)


T = I()
for ___ in range(T):
    solve()
