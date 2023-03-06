n = int(input())
string = list(input().split())
q = int(input())
qry = []
for index in range(q):
    qry.append(input())
 
 
for index in range(q):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low)//2
        if string[mid] < qry[index]:
            low = mid + 1
        else:
            high = mid - 1
    print(low)