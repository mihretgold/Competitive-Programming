class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = defaultdict(int)
        def calc(index, transaction):
            current_profit = 0
            if (index, transaction) in mem:
                return mem[(index, transaction)]
                
            if index >= len(prices):
                return 0

            if transaction == 0:
                val1 = calc(index + 1, 0) 
                val2 = calc(index + 1, 1) - prices[index]
                current_profit = max(val1, val2)

            if transaction == 1:
                val1 = calc(index + 1, 1)
                val2 = calc(index + 2, 0) + prices[index]
                current_profit = max(val1, val2)

            mem[(index, transaction)] =  current_profit
            return mem[(index, transaction)]

        return calc(0, 0)