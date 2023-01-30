t = int(input())
for i in range(t):
    string = input()
    n = len(string)
    work = set()
    left = 0
    while left < n:
        if left+1 == n or string[left] != string[left+1]:
            work.add(string[left])
            left += 1
        else:
            left += 2
 
    list_set = list(work)
    list_set.sort()
    ans = "".join(list_set)
    print(ans)
