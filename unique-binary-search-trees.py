class Solution:
    "-1 root 0 left 1 right"
    def numTrees(self, n: int) -> int:
        mem = defaultdict(int)
        def calcPermute(n):
            if n <= 1:
                return 1
            
            if n == 2:
                return 2

            if n in mem:
                return mem[n]

            total = 0
            for root in range(1, n+1):
                left = calcPermute(root - 1)
                right = calcPermute(n - root)

                total += left*right

            mem[n] = total
            return mem[n]

        return calcPermute(n)