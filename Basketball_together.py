from collections import defaultdict
N, D = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse= True)
count = 0
for i in range(len(a)):
    if (D//a[i]) + 1 <= N:
        count += 1
        N -= (D//a[i]) + 1
    else:
        break
 
print(count)