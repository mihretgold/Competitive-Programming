class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = defaultdict(int)
        def dp(target):
            if target == 0:
                return 0
            if target < 0:
                return float('inf')

            if target in mem:
                return mem[target]

            mini = float('inf')
            for coin in coins:
                mini = min(mini, dp(target-coin)+1)

            mem[target] = mini
            return mem[target]
        answer = dp(amount)
        
      
        return answer if answer != float('inf') else -1