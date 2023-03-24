def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def IS(): return  input()
def SIL(): return sorted(map(int, input().split()), reverse= True)

def solve():
    n, m = II()
    freq = IL()
    cost = IL()
    queries = []
    for _ in range(m):
        a, b = II()
        queries.append([a, b])
    cheapest = []
    for i in range(n):
        cheapest.append((cost[i], i))

    cheapest.sort()
    i = 0
    for a, b in queries:
        price = 0
        val = freq[a-1]
        if val >= b:
            price += (cost[a-1]*b)
            freq[a-1] -= b
            b = 0
        else:
            price += (cost[a-1] * val)
            b -= val
            freq[a-1] = 0


        while b > 0:
            food = None
            while i < n and food == None:
                minCost, food = cheapest[i]
                if freq[food] == 0:
                    food = None
                    i += 1
                else:
                    break
            if food == None:
                price = 0
                break

            if freq[food] >= b:
                price += (cheapest[i][0]*b)
                freq[food] -= b
                b = 0
            else:
                price += (cheapest[i][0]*freq[food])
                b -= freq[food]
                freq[food] = 0




        if b > 0:
            price = 0
        print(price)


T = 1
for ___ in range(T):
    solve()