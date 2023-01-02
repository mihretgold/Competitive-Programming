from collections import defaultdict
t = int(input())

for i in range(t):
    count = 0
    orbit = defaultdict(int)
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    for planet in arr:
        orbit[planet] += 1
    for planet in orbit:
        if orbit[planet] >= c:
            count += c
        else:
            count += orbit[planet]
    print(count)
