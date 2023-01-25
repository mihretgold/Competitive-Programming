n = int(input())
nums = list(map(int, input().split()))
nums.sort()
if nums[-2] + nums[-3] > nums[-1]:
    print("YES")
    temp = nums[-2]
    nums[-2] = nums[-1]
    nums[-1] = temp
    print(*nums)
else:
    print("NO")
