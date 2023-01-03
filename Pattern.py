n = int(input())
pattern = []
for i in range(n):
    string = input()
    pattern.append(string)

answer = ''
m = len(pattern[0])
for i in range(m):
    set_p = set() 
    for j in range(n):
        if pattern[j][i] != '?':
            set_p.add(pattern[j][i])
    size = len(set_p)
    if size == 1:
        for word in set_p:
            answer += str(word)
    elif size == 0:
         answer += 'd'
    elif size > 1:
         answer += '?'
print(answer)
