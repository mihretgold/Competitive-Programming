t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    sums = sum(nums)
    sums -= nums[-1]
    left = 0
    count = sums
    for right in range(1, n-1):
        while nums[left] == 0 and left < right:
            left += 1
        if nums[right] == 0 and nums[left] != 0:
            count += 1
    print(count)