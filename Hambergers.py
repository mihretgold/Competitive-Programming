from collections import Counter
def check(mid, rb, rs, rc, nb, ns, nc, pb, ps, pc, r):
    # number of ingridients needed mid number burger
    b = rb*mid - nb
    s = rs*mid - ns
    c = rc*mid - nc
 
    if b < 0:
        b = 0
    if s < 0:
        s = 0
    if c < 0:
        c = 0
    # prices of ingridients needed mid number burger
    price_b = b * pb
    price_s = s * ps
    price_c = c * pc
    total = price_b + price_c + price_s
    return total <= r
 
 
 
def main():
    order = input()
    count = Counter(order)
    nb, ns, nc = map(int, input().split())
    pb, ps, pc = map(int, input().split())
    r = int(input())
    low = 0
    high = 1e14
    while low <= high:
        mid = low + (high - low)//2
        if check(mid,count["B"], count["S"], count["C"], nb, ns, nc, pb, ps, pc, r):
            low = mid + 1
        else:
            high = mid - 1
 
    print(int(low-1))
main()