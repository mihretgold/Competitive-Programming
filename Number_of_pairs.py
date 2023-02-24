
from collections import defaultdict
n = int(input())
b = list(map(int,input().split()))
m = int(input())
g = list(map(int,input().split()))
b.sort()
g.sort()
i = 0
j = 0
pair = 0
 
while i < n and j < m:
    if abs(b[i] -g[j]) <= 1:
        pair += 1
        i += 1
        j += 1
    elif b[i] < g[j]:
        i += 1
    else:
        j += 1
 
print(pair)
