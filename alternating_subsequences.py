tt = int(input())
 
while tt:
 
    n = int(input())
    a = list(map(int, input().split()))
    ptr = 0
    ans = []
    while ptr<n:
        if a[ptr]<0:
            Max = float('-inf')
            while ptr<n and a[ptr]<0:
                Max = max(Max, a[ptr])
                ptr+=1
            ans.append(Max)
        else:
            Max = float('-inf')
            while ptr<n and a[ptr]>0:
                Max = max(Max, a[ptr])
                ptr+=1
            ans.append(Max)
    print(sum(ans))
        
    tt-=1
