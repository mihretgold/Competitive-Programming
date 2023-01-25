t = int(input())
for i in range(t):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[1])
