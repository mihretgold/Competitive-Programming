from collections import Counter
q = int(input())
for i in range(q):
    n = int(input())
    a= list(map(int, input().split()))
    a.sort()
    start = 0
    end = len(a)-1
    sums = set()
    while start <= end:
        sums.add(a[start] * a[end])
        start += 2
        end -= 2
    count = Counter(a)
    found = 0
    for num in count:
        if count[num] % 2 != 0:
            found = -1
            break
 
    if len(sums) == 1 and found == 0:
        print("YES")
    else:
        print("NO")