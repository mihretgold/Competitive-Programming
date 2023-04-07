class Solution:
    def sieve(self, n: int)-> list[bool]:
        prime: list[bool] = [True for _ in range(n + 1)]
        prime[0] = prime[1] = False
        d = 2
        while d * d <= n:
            if prime[d]:
                j = d * d
                while j <= n:
                    prime[j] = False
                    j += d
            d += 1

        return  prime

    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = self.sieve(right)
        primes = []
        answer = [-1, -1]

        for index in range(left, right+1):
            if arr[index]:
                primes.append(index)
                if len(primes) > 1:
                    if answer[-1] - answer[-2] == 0 or  answer[-1] - answer[-2] > primes[-1] - primes[-2]:
                        answer = [primes[-2], primes[-1]]



        return answer