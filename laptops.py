n = int(input())
lap_top = []
for i in range(n):
    a, b = map(int, input().split())
    lap_top.append([b, a])
lap_top.sort(reverse=True)
 
for index in range(n-1):
    if lap_top[index][1] < lap_top[index + 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
