import math
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
def factors(num):
    answer = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            answer.append(i)
            if i != num // i:
                answer.append(num//i)
 
    return answer
 
 
def solve():
  n = I()
  factorsList = factors(n)
  answer = [1, n]
  for a in factorsList:
      b = n//a
      if math.gcd(a, b) == 1 and max(a, b) < max(answer[0], answer[1]):
          answer = [a, b]
 
  print(*answer)
 
 
 
T = 1
for ___ in range(T):
    solve()