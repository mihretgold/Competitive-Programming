class Solution:
    def __init__(self):
        self.mem = defaultdict(int)

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in self.mem:
            return self.mem[n]

        self.mem[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.mem[n]