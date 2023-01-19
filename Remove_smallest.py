t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    nums.sort()
    for index in range(n-1):
        if abs(nums[index+1] - nums[index]) <= 1:
            count += 1
        
    if count >= n-1:
        print("YES")
    else:
        print("NO")
