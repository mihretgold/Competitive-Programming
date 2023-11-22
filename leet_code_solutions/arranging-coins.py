class Solution:
    def arrangeCoins(self, n: int) -> int:
        # brute force recursion

        # def calc(n, take):
        #     if n <= take:
        #         return take - 1

        #     return calc(n - take, take + 1)

        # return calc(n, 1)

        # binary search

        low = 1
        high = n

        while low <= high:
            mid = low + (high - low)//2

            calc = ((mid + 1) * mid)//2
            if calc <= n:
                low = mid + 1
            else:
                high = mid - 1

      

        return high 
        