from collections import defaultdict
a, b, c = map(int, input().split())
count_a = a + c
count_b = b + c
if count_a == count_b:
    print(count_b + count_a)
elif count_a < count_b:
    print((count_a + 1) + count_a)
elif count_b < count_a:
    print((count_b + 1) + count_b)
