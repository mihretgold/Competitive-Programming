from collections import defaultdict
n = int(input())
nums = list(map(int,input().split()))
sort_list = sorted(nums)
fsum = 0
bsum = 0
 
for i in range(n):
    fsum += sort_list[i]
 
for i in range((2*n)-1, n-1, -1):
    bsum += sort_list[i]
 
 
if fsum == bsum:
    print(-1)
else:
    print(*sort_list)
