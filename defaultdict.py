# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m=map(int,input().split(' '))
d = defaultdict(list)

for index in range(n):
    A = input()
    d[A].append(index + 1)
    
for index in range(m):
    B = input()
    if d[B]:
        print(*d[B])
    else:
        print(-1)
     
