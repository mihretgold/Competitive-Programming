class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            d = 2
            while d * d <= num:
                while num % d == 0:
                    unique.add(d)
                    num //= d

                d += 1

            if num != 1:
                unique.add(num)
        return len(unique)