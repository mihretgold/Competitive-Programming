def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()), reverse= True)
 
def solve():
   n, k = II()
   a = SIL()
   curr = 2 ** n
   total = 0
   while k > 0:
       curr //= 2
       total += min(k, curr) * a[curr]
       k -= min(k, curr)
   print(total)
 
T = 1
for ___ in range(T):
    solve()