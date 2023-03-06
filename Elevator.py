
t = int(input())
for i in range(t):
    wt, et, ef = map(int, input().split())
    elevator = (ef * et) + 4 * et
    floor = wt * 4
    elf = (ef * wt) + (4-ef) * et
    ans = min(floor, elf, elevator)
    print(ans)