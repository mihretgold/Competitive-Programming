n = int(input())
card = list(map(int, input().split()))
end = n-1
start = 0
wube = 0
henok = 0
count = 0
while start <= end:
    if card[start] >= card[end]:
        if count % 2 == 0:
            wube += card[start]
        else:
            henok += card[start]
        start += 1
    else:
        if count % 2 == 0:
            wube += card[end]
        else:
            henok += card[end]
        end -= 1
    count += 1
 
print(wube, henok)
