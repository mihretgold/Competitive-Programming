class Solution:
    def __init__(self):
        self.mem = defaultdict(int)

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        if (m, n) in self.mem:
            return self.mem[(m, n)]
        answer = 0
        if n-1 > 0:
            answer += self.uniquePaths(m, n-1) 
        if m - 1 > 0:
            answer += self.uniquePaths(m-1, n)
        
        self.mem[(m, n)] = answer
        return self.mem[(m, n)]