def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter

def solve():
  x = I()
  if x == 1:
      print(3)
  elif x & (x-1) == 0:
      print(x+1)
  else:
      string = bin(x)
      answer = ""
      for i in range(len(string)-1, -3, -1):
          if string[i] == "0":
              answer += "0"
          else:
              answer += "1"
              break

      answer = answer[::-1]
      print(int(answer,2))

T = I()
for ___ in range(T):
    solve()