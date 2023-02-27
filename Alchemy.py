n = int(input())
nums = list(map(int, input().split()))
s = 0
e = n-1
alp = 0
ed = 0
alp_count = 0
ed_count = 0
while s <= e:
    if alp <= ed:
       alp += nums[s]
       alp_count += 1
       s += 1
 
       # print(1,nums[s])
    else:
        ed += nums[e]
        ed_count += 1
        e -= 1
 
        # print(2,nums[e])
 
 
print(alp_count, ed_count)
