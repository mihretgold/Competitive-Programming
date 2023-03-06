t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
 
    index = 0
    counts = 0
    sums = 2
 
    if n <= sums:
        print(0)
    else:
        while index < m:
            sums += nums[index] - 1
            counts += 1
 
            if sums >= n:
                break
 
            index += 1
 
        if sums >= n:
            print(counts)
        else:
            print(-1)