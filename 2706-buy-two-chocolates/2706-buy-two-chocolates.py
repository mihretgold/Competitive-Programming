class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        answer = prices[0] + prices[1]
        
        if answer <= money:
            return money - answer
        else:
            return money
        
         