from collections import defaultdict
t = int(input())
 
for index in range(t):
    n, m, k = map(int, input().split())
    a = list(input())
    b = list(input())
    a.sort()
    b.sort()
 
    i = 0
    j = 0
    acount = 0
    bcount = 0
    res = ""
 
    while i< n and j < m:
        if a[i] < b[j] and acount < k:
          res += a[i]
          i += 1
          acount += 1
          bcount = 0
        elif b[j] < a[i] and bcount < k:
            res += b[j]
            j += 1
            bcount += 1
            acount = 0
        elif acount == k:
            res += b[j]
            j += 1
            acount = 0
        elif bcount == k:
            res += a[i]
            i += 1
            bcount = 0
 
    print(res)
