from collections import defaultdict
x = int(input())
ans = ''
string = str(x)
for j,val in enumerate(string):
    if j == 0 and val == '9':
        ans += val
    else:
        num = min(int(val), 9 - int(val))
        ans += str(num)
print(ans)
