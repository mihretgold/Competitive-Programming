class Solution:
    def sieve(self, n: int)-> list[bool]:
        prime: list[bool] = [True for _ in range(n)]
        if n > 0:
            prime[0] = False
        if n > 1:
            prime[1] = False
        d = 2
        while d * d <= n:
            if prime[d]:
                j = d * d
                while j <= n-1:
                    prime[j] = False
                    j += d
            d += 1

        return  prime
    def countPrimes(self, n: int) -> int:
        prime = self.sieve(n)
        countPrimes = 0
        for index in range(n):
            if prime[index]:
                countPrimes += 1

        return countPrimes