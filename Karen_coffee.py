n, k, q = map(int, input().split())
prefix = [0 for i in range(200002)]
recipes = []
questions = []
 
for i in range(n):
    a, b =  map(int, input().split())
    recipes.append([a, b])
for i in range(q):
    a, b =  map(int, input().split())
    questions.append([a, b])
 
for a, b in recipes:
    prefix[a] += 1
    prefix[b+1] -= 1
 
for i in range(1, 200002):
    prefix[i] += prefix[i-1]
 
for i in range(200002):
    if prefix[i] >= k:
        prefix[i] = 1
    else:
        prefix[i] = 0
 
for i in range(1, 200002):
    prefix[i] += prefix[i-1]
 
for a, b in questions:
    count = prefix[b] - prefix[a-1]
    print(count)