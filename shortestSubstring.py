t = int(input())
for i in range(t):
    string = input()
    n = len(string)
    rigth = 0
    left = 0
    co = 0
    ct = 0
    cth = 0
    mini = float('inf')
    for rigth in range(n):
        if string[rigth] == "1":
            co += 1
        elif string[rigth] == "2":
            ct += 1
        else:
            cth += 1
        # print("r", rigth)
        rigth += 1
        while co > 0 and ct > 0 and cth > 0:
            ans = rigth - left
            # print("a", ans)
            mini = min(ans, mini)
            if string[left] == "1":
                co -= 1
            elif string[left] == "2":
                ct -= 1
            else:
                cth -= 1
            left += 1
 
 
 
    if mini == float('inf'):
        mini = 0
    print(mini)
