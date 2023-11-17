class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append(value)
        self.timestamps[key].append(timestamp)

    def bisect(self, arr, search):
        low = 0
        high = len(arr) - 1
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] <= search:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.timestamps[key]
        if timestamp >= arr[-1]:
            return self.store[key][-1]

        low = 0
        high = len(arr) - 1
        ans = self.bisect(arr, timestamp)

        return "" if ans < 0 else self.store[key][ans]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)