t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    string = input()
    string = '0' + string + '0'
    string = list(string)
    check = []
    m = min(m, n)
    for _ in range(m):
        count = 0
        for index in range(1, n+1):
            if string[index] == "0" and ((string[index + 1] == "1" and string[index -1] == "0") or (string[index + 1] == "0" and string[index -1] == "1")):
                check.append(index)
                count += 1
        for i in range(len(check)):
            string[check[i]] = '1'
        if count == 0:
            break
    print("".join(string[1:-1]))