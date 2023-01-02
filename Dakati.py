from collections import defaultdict
t = int(input())
for index in range(t):
    chorus = input().split()
    ans = []
    for string in chorus:
        length = len(string)
        for i in range(length):
           if string[i].isdigit():
             word = ''
             word = word + string[i] + string[:i] + string[i+1:]
             ans.append(word)
    ans.sort()
    answer = ' '.join(ans)
    for i in answer:
        if i.isdigit():
            answer = answer.replace(i,'')
    print(answer)
