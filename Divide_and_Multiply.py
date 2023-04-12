import math
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
 
def solve():
   n = I()
   a = SIL()
   count = 0
   i = 0
   maxi = 0
 
   while i < n:
       if a[i] & 1 == 0:
           a[i] //= 2
           count += 1
       if a[i] & 1 != 0:
           if a[i] > a[maxi]:
               maxi = i
           i += 1
 
   a[maxi] = a[maxi] * 2**count
   answer = sum(a)
   print(answer)
 
 
 
 
T = I()
for ___ in range(T):
    solve()