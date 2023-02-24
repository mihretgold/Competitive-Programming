t = int(input())
 
for i in range(t):
    l1, w1 = map(int, input().split())
    l2, w2 = map(int, input().split())
 
    if l1 == w1:
        print("No")
    elif l1 == l2 and (w1 + w2) == l1:
        print("Yes")
    elif l1 == w2 and (l2 + w1) == l1:
        print("Yes")
    elif w1 == l2 and (l1 + w2) == l2:
        print("Yes")
    elif w1 == w2 and (l2 + l1) == w1:
        print("Yes")
    else:
