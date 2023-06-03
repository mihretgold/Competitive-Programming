class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        mem = defaultdict(int)
        def calcProfit(index, b_s):
            currentBalance = 0
            if index > len(prices)-1:
                return 0

            if (index, b_s) in mem:
                return mem[(index, b_s)]
            
            if b_s == 0:
                val1 = calcProfit(index + 1, 0)
                val2 = calcProfit(index + 1, 1) - fee - prices[index]
                currentBalance = max(val1, val2) 
            if b_s == 1:
                val3 = calcProfit(index + 1, 1)
                val4 = calcProfit(index + 1, 0) + prices[index]
                currentBalance = max(val3, val4) 

            mem[(index, b_s)] = currentBalance
            return mem[(index, b_s)]

        return calcProfit(0, 0)