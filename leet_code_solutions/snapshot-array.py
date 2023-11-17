class SnapshotArray:

    def __init__(self, length: int):
        self.store = [[[0, 0]] for _ in range(length)]
        self.count=0

    def set(self, index: int, val: int) -> None:
        self.store[index].append([self.count, val])
        
    def snap(self) -> int:
        self.count += 1 
        
        return self.count - 1

    def get(self, index: int, snap_id: int) -> int:
        low = 0 
        arr = self.store[index]
        
        high = len(arr) - 1
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
           
            if arr[mid][0] <= snap_id:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        
        return self.store[index][ans][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)