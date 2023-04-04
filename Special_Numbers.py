def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
def solve():
    a, b = II()
    string = bin(b)[2:]
    answer = 0
    length = len(string)
    for index in range(length):
        power = (length-1) - index
        if string[index] == "1":
            answer += a ** power
 
    print(answer % (10**9 + 7))
 
 
 
 
T = I()
for ___ in range(T):
    solve()
