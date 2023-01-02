from collections import defaultdict
n = int(input())
points = list(map(int, input().split()))
maxi = points[0]
mini = points[0]
count = 0
for index in range(1, n):
   if points[index] > maxi:
       maxi = points[index]
       count += 1
   elif  points[index] < mini:
       mini = points[index]
       count += 1
 
print(count)
