n = int(input())
nums = list(map(int,input().split()))
pos = 0
neg = 0
zero = 0
maxi = float('-inf')
sum = 0
cnt = 0
for i in range(n):
    if nums[i] > 0:
        pos += 1
    elif nums[i] < 0:
        neg += 1
        maxi = max(maxi, nums[i])
    else:
        zero += 1
for i in range(n):
    if neg % 2 != 0 and nums[i] == maxi and cnt == 0 and zero == 0:
        sum += abs(1 - nums[i])
        cnt += 1
    elif nums[i] > 0:
        sum += abs(1 - nums[i])
    elif nums[i] < 0:
        sum += abs(-1 - nums[i])
    else:
        sum += 1
 
print(sum)
