n, k = map(int,input().split())
lecture = list(map(int, input().split()))
wake =  list(map(int, input().split()))
sum = 0 
maxi = 0
size = len(wake)

for i in range(size):
    if wake[i] == 1:
        sum += lecture[i]

i = 0 
j = 0
while j < size:
    if wake[j] == 0:
        sum += lecture[j]
        
    if j- i >= k:
        if wake[i] == 0:
            sum -= lecture[i]
        i += 1
    maxi = max(maxi,sum)
    j += 1
    
print(maxi)

 


