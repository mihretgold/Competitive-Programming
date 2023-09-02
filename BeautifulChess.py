t = int(input())
for a in range(t):
    empty = input()
    chess = []
    for i in range(8):
        temp = input()
        chess.append(temp)
 
    for i in range(1, 7):
       for j in range(1, 7):
           if chess[i-1][j+1] == '#' and chess[i-1][j-1] == '#' and chess[i+1][j-1] == '#' and chess[i+1][j+1] == '#':
               print(i+1, j+1)