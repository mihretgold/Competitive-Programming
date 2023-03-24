def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()), reverse= True)
 
count = 0
 
def mergeSort(arr, low, high):
    if low == high:
        return [arr[low]]
    mid = low + (high - low)//2
    left = mergeSort(arr, low, mid)
    right = mergeSort(arr, mid+1, high)
    return merge(left, right)
 
def merge(left, right):
    global count
    answer = []
    if left[0] < right[0]:
        answer = left + right
    else:
        count += 1
        answer = right + left
 
    return answer
 
def solve():
   global count
   n = I()
   a = IL()
   answer = mergeSort(a, 0, n-1)
   a.sort()
   if answer == a:
       print(count)
   else:
       print(-1)
 
 
 
 
T = I()
for ___ in range(T):
    solve()
    count = 0