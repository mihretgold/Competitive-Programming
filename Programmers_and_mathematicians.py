t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    low = 0
    high = (a + b)//4
    while low <= high:
        mid = low + (high - low)//2
        if mid <= min(a, b):
            low = mid + 1
        else:
            high = mid - 1
 
    print(high)