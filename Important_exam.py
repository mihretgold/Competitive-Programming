from collections import defaultdict
n, m = map(int, input().split())
lis = []
 
for i in range(n):
    string = input()
    lis.append(string)
a = list(map(int,input().split()))
r_l = len(lis[0])
c_l = len(lis)
sum = 0
for i in range(r_l):
    dict = defaultdict(int)
    for j in range(c_l):
        dict[lis[j][i]] += 1
    sum += max(dict.values()) * a[i]
print(sum)
