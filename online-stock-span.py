class StockSpanner:

    def __init__(self):
        self.stock = []
        self.count = 0

    def next(self, price: int) -> int:
        top = 0
        ans = 1
        while self.stock and self.stock[-1][0] <= price:
            self.stock.pop() 

        if self.stock:
            top = self.stock[-1][1]
            ans = self.count - top
        else:
            ans = self.count + 1
        self.stock.append((price, self.count))
        self.count += 1
        
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)