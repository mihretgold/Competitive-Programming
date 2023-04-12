import math
 
 
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
from collections import defaultdict
from collections import Counter
 
def factors(num):
    answer = []
    answer.append(num)
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            answer.append(i)
            if i != num // i:
                answer.append(num//i)
 
    return answer
 
def solve():
    a, b = II()
    n = I()
    aList = factors(a)
    bList = factors(b)
    bList = set(bList)
    check = set()
    for num in aList:
        if num in bList:
            check.add(num)
    check = list(check)
    check.sort()
    for _ in range(n):
        low, high = II()
        left = 0
        right = len(check) - 1
        while left <= right:
            mid = left + (right - left)//2
            if check[mid] <= high:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0 and check[right] >= low and check[right] <= high:
            print(check[right])
        else:
            print(-1)
 
 
 
 
 
 
 
T = 1
for ___ in range(T):
    solve()