
from collections import defaultdict
 
n, m = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
map_toy = defaultdict(int)
for i in range(m):
    toy = input()
    map_toy[toy] += 1
 
sort_map = sorted(map_toy.items(), key= lambda kv: kv[1])
sort_map.reverse()
 
mini = 0
maxi = 0
i = 0
for ty in sort_map:
    mini += ty[1] * num[i]
    i += 1
 
 
i = n-1
for ty in sort_map:
    maxi += ty[1] * num[i]
    i -= 1
 
print(mini, maxi
