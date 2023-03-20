from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
l = 0
ans = [1, 1]
maxi = 0
set_k = defaultdict(int)
for r in range(n):
    set_k[a[r]] += 1
    while len(set_k) > k:
        set_k[a[l]] -= 1
        if set_k[a[l]] == 0:
            set_k.pop(a[l])
        l += 1
    if (r - l + 1) > maxi:
        maxi = r - l + 1
        ans = [l+1, r+1]
 
print(ans[0], ans[1])