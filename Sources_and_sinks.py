import math
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter

def solve():
   n = I()
   sourceNeg = set()
   sinkNeg = set()

   for index in range(n):
       nums = IL()
       for num in range(len(nums)):
            if nums[num] == 1:
                sourceNeg.add(num+1)
                sinkNeg.add(index+1)
   source = []
   sink = []
   for index in range(n):
       if index + 1 not in sourceNeg:
           source.append(index+1)
       if index + 1 not in sinkNeg:
           sink.append(index+1)


   print(len(source),*source)
   print(len(sink), *sink)





T = 1
for ___ in range(T):
    solve()