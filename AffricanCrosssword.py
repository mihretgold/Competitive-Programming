from collections import defaultdict
n, m = map(int, input().split())
crossword = []
for i in range(n):
    temp = list(input())
    crossword.append(temp)

duplicates = set()
for i in range(n):
    check = defaultdict(list)
    for j in range(m):
        if crossword[i][j] in check:
            duplicates.add((i, j))
            duplicates.add((check[crossword[i][j]][0], check[crossword[i][j]][1]))
        else:
            check[crossword[i][j]] = [i, j]

for i in range(m):
    check = defaultdict(list)
    for j in range(n):
        if crossword[j][i] in check:
            duplicates.add((j, i))
            duplicates.add((check[crossword[j][i]][0], check[crossword[j][i]][1]))
        else:
            check[crossword[j][i]] = [j, i]

ans = ""
for i in range(n):
    for j in range(m):
        if (i, j) not in duplicates:
            ans += crossword[i][j]

print(ans)



