class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        mem = defaultdict(int)
        mem[0] = 0
        mem[1] = 1
        maxi = 0

        for index in range(2, n+1):
            if index & 1 == 0:
                mem[index] = mem[index//2]
            else:
                mem[index] = mem[index//2] + mem[index//2 + 1]

            maxi = max(maxi, mem[index])

        if n == 1:
            maxi = 1
        return maxi