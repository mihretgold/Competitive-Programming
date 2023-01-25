n = int(input())
a = list(map(int, input().split()))
left = 0
right = n - 1
sort_list = sorted(a)
if a == sort_list:
    print("yes")
    print(1, 1)
else:
    for i in range(1, n):
        if a[i-1] > a[i]:
            left = i-1
            break
 
    for i in range(n-1, 0, -1):
        if a[i] < a[i-1]:
            right = i
            break
 
    reverse =  a[left:right+1][::-1]
    check = a[:left] + reverse + a[right+1:]
 
    if check == sort_list:
        print("yes")
        print(left+1, right+1)
    else:
        print("no")
