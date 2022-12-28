A = set(map(int,input().split(' ')))
n = int(input())
check1 = True
length_A = len(A)

for sets in range(n):
    B = set(map(int,input().split(' ')))
    length_B = len(B)
    if B - A or length_A <= length_B:
        check1 = False
        break
print(check1)
