from functools import reduce
from operator import mul
class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        for index in range(1, n):
            dp[index] = (index + 1) * ((2* (index + 1)) - 1) * dp[index - 1]  % (10 ** 9 +  7)

        
        return dp[n-1] % (10 ** 9 +  7)