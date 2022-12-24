n=int(input())
for x in range(n):
    m=int(input())
    sideLength=list(map(int ,input().split()))
    check=True
    l=0
    r=len(sideLength)-1
    while(l<r):
        large=max(sideLength[l],sideLength[r])
        if sideLength[l]>sideLength[r]:
            l+=1
        else:
            r-=1
        if sideLength[l]>large or sideLength[r]>large:
            check=False
            break
    if check:
        print("Yes")
    else:
        print("No")
