def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
 
def merge(arr, left, right, k):
    answer = []
    i = 0
    j = 0
    lengthL = len(left)
    lengthR = len(right)
 
    while (i < lengthL and j < lengthR) and arr[left[i]] - arr[right[j]] > k:
        j += 1
 
    while (i < lengthL and j < lengthR) and arr[right[j]] - arr[left[i]] > k:
        i += 1
 
    while i < lengthL or j < lengthR:
        if j == lengthR or (i < lengthL and arr[left[i]] <= arr[right[j]]):
            answer.append(left[i])
            i += 1
        else:
            answer.append(right[j])
            j += 1
 
    return answer
 
 
 
 
def mergeSort(l, h, k, arr):
    if l == h:
        return  [l]
    mid = (l + h)//2
    left = mergeSort(l, mid, k, arr)
    right = mergeSort(mid + 1, h , k, arr)
    answer = merge(arr, left, right, k)
 
    return answer
 
def solve():
   n, k = II()
   a = IL()
   answer = mergeSort(0, 2**n - 1, k, a)
   answer.sort()
   func = lambda x: x+1
   answer = list(map(func, answer))
 
   print(*answer)
 
 
 
T = 1
for ___ in range(T):
    solve()