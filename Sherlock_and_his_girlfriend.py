def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
 
def solve():
   n = I()
   prime = [1 for _ in range(n+2)]
   prime[0] = prime[1] = 0
   d = 2
   color = 2
   while d * d <= n+1:
       if prime[d] == 1:
           j = d * d
           while j <= n+1:
               # check
               prime[j] = color
               j += d
       d += 1
           # color += 1
   print(len(set(prime[2:])))
   print(*prime[2:])
 
 
 
 
T = 1
for ___ in range(T):
    solve()
