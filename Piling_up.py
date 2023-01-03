n=int(input())
for x in range(n):
    m=int(input())
    sideLength=list(map(int ,input().split()))
    check=float('INF')
    l=0
    r=len(sideLength)-1
    count = 0
    while(l <= r):
        if sideLength[r] >= sideLength[l] and sideLength[r] <= check:
            check = sideLength[r]
            r -= 1
            count += 1
        elif sideLength[l] <= check:
            check = sideLength[l]
            l += 1
            count += 1
        else:
            break
    if count == len(sideLength):
        print("Yes")
    else:
        print("No")
