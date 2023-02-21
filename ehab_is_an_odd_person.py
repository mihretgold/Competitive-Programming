n = int(input())
nums = list(map(int, input().split()))
odd = 0
even = 0
for i in range(n):
    if nums[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if odd != 0 and even != 0:
    nums.sort()
print(*nums)
