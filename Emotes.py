n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
x = m//(k+1)
if n > 1:
    ans += x * a[-2]
    ans += (m-x) * a[-1]
else:
    ans += k * a[0]
print(ans)