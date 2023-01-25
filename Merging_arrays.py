n, m = map(int, input().split());
a = list(map(int,input().split()));
b = list(map(int,input().split()));
i = 0;
j = 0;
ans = [];
while(i<n and j<m):
    if a[i] <= b[j]:
        ans.append(a[i])
        i += 1
    elif b[j] < a[i]:
        ans.append(b[j])
        j += 1
        
ans.extend(a[i:])
ans.extend(b[j:])
    
print(*ans); 
