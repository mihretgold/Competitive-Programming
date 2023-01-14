t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    listNum = []
    for i in range(n):
        temp = list(map(int, input().split()))
        listNum.append(temp)

        diagonal = [0 for _ in range(m + n - 1)]
        antiDiagonal = [0 for _ in range(m + n - 1)]
        for i, row in enumerate(listNum):
            for j, num in enumerate(row):
                diagonal[i - j] += num
                antiDiagonal[i + j] += num

        maxi = 0
        for i, row in enumerate(listNum):
            for j, num in enumerate(row):
                sum = diagonal[i - j] + antiDiagonal[i + j] - num
                maxi = max(sum, maxi)
    print(maxi)
