n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
left = 0
right = 1

while right < n:
    if right == k:
        if nums[right] == nums[left]:
            print(-1)
            break
        else:
            print(nums[left])
    right += 1
    left += 1
if k == 0:
    if nums[0] == 1:
        print(-1)
    else:
        print(1)
elif n == 1 and k > 0:
    print(nums[0])
elif n == k:
    print(nums[-1])
