class DetectSquares:

    def __init__(self):
        self.counter = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counter[(x, y)] += 1
        

    def count(self, point: List[int]) -> int:
        answer = 0
        x, y = point
        print(self.counter)
        for (valx, valy), count in self.counter.items():
            if valx != x and abs(x - valx) == abs(y - valy) and (x, valy) in self.counter and (valx, y) in self.counter:
                answer += self.counter[(x, valy)] * self.counter[(valx, y)] * count


        return answer
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)