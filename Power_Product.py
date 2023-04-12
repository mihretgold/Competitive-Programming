import math
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter

def solve():
  n, k = II()
  numbers = IL()
  count = 0
  nums = defaultdict(int)

  for index in range(n):
      power = defaultdict(int)
      d = 2
      while d * d <= numbers[index]:
         while numbers[index] % d == 0:
             power[d] += 1
             numbers[index] //= d

         d += 1

      if numbers[index] != 1:
          power[numbers[index]] += 1

      product = 1
      key = 1

      for number in power:
          exponent = power[number]
          modulo = exponent % k
          if modulo != 0:
            product *= (number ** (k - modulo))
          key *= number ** (power[number] % k)
      count += nums[product]
      nums[key] += 1


  print(count)



T = 1
for ___ in range(T):
    solve()


