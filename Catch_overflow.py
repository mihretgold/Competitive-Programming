from sys import stdin
t = int(input())
stack = [[1,0]]
for _ in range(t):
    comand = stdin.readline().strip()
    if comand == "add":
        stack[-1][1] += 1
    elif comand == "end":
        iterations, num = stack.pop()
        stack[-1][1] += iterations * num
    else:
        cmd, num = comand.split()
        stack.append([int(num), 0])

if stack[-1][1] > (2**32 -1):
    print("OVERFLOW!!!")
else:
    print(stack[-1][1])