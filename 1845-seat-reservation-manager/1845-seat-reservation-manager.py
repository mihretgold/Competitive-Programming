class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        
        for index in range(1, n + 1):
            heappush(self.heap, index)
        

    def reserve(self) -> int:
        seat = heappop(self.heap)        
        
        return seat        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)