
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    # print(nums)
    s = 0
    e = n-1
    ans = []
    while s <= e:
        if s == e:
            ans.append(nums[s])
            s += 1
        else:
            ans.append(nums[s])
            s += 1
            ans.append(nums[e])
            e-=1
 
    print(*ans)
