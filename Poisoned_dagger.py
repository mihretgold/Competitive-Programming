def check(h, k, arr):
    count = k
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] <= k:
            count += (arr[i+1] - arr[i])
        else:
            count += k
    return count >= h
 
t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    low = 0
    high = h
 
    while low <= high:
        mid = low + (high - low)//2
        if check(h, mid, a):
            high = mid -1
        else:
            low = mid + 1
 
    print(int(low))