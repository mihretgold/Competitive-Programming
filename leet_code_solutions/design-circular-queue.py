class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.start = 0
        self.length = k     
        self.end = 0

    def enQueue(self, value: int) -> bool:
        if not (self.end % self.length == self.start % self.length and self.arr[self.end % self.length] != -1):
            self.arr[self.end % self.length] = value
            self.end += 1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if not (self.end % self.length == self.start % self.length and self.arr[self.end % self.length] == -1):
            self.arr[self.start % self.length] = -1
            self.start += 1
            return True
        else:
            return False

    def Front(self) -> int:
        return self.arr[(self.start) % self.length]
        

    def Rear(self) -> int:
        return self.arr[(self.end - 1) % self.length]
        

    def isEmpty(self) -> bool:
        return  (self.end % self.length == self.start % self.length and self.arr[self.end % self.length] == -1)
       

    def isFull(self) -> bool:
        return  (self.end % self.length == self.start % self.length and self.arr[self.end % self.length] != -1)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()