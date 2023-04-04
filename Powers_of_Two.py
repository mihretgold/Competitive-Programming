def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
def solve():
    n, k = II()
    string = bin(n)[2:]
 
    if k >= string.count("1") and k <= n:
        print("YES")
        string = bin(n)[2:]
        res = []
        ones = []
 
        length = len(string)
 
        for i in range(length-1):
            power = ((length-1) - i)
            if string[i] == "1":
                ans = 1*(2**power)
                res.append(ans)
 
        if n & 1 != 0:
            ones.append(1)
 
        while len(res) + len(ones) < k:
            if res[-1] == 2:
                res.pop()
                ones.append(1)
                ones.append(1)
            else:
                val = res[-1] // 2
                res[-1] = val
                res.append(val)
 
        answer = res + ones
        print(*answer)
 
    else:
        print("NO")
 
 
T = 1
for ___ in range(T):
    solve()