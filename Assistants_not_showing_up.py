n, m = map(int, input().split())
queries = []
for i in range(m):
    a, b = map(int, input().split())
    queries.append([a, b])
 
prefix = [0 for _ in range(n)]
for a, b in queries:
    prefix[a] += 1
    if b+1 <= n-1:
        prefix[b+1] -= 1
 
for i in range(1, n):
    prefix[i] += prefix[i-1]
 
 
if min(prefix) == 0:
    print("YES")
else:
    print("NO")