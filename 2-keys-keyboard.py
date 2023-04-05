class Solution:
    def minSteps(self, n: int) -> int:
        total = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                total += d
                n //= d

            d += 1

        if n != 1:
            total += n

        return total