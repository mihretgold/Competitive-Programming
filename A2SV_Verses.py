n, a, b = map(int, input().split())
nums = list(map(int, input().split()))
start = 0
count = 0
sums = 0
for end in range(n):
    sums += nums[end]
    while sums > b:
        sums -=nums[start]
        start += 1
 
    count += end - start + 1
start = 0
count2 = 0
sums = 0
for end in range(n):
    sums += nums[end]
    while sums >= a:
        sums -= nums[start]
        start += 1
 
    count2 += end - start + 1
 
print(count - count2)