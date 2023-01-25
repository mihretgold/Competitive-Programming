t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    left = 0
    count = 0
    sort_two = list(map(int, input().split()))
    for right in range(1, n):
        if sort_two[right-1] >= 2*sort_two[right]:
            left = right
        while right-left == k:
            count += 1
            left += 1
 
    print(count)
