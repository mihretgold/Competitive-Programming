from sortedcontainers import SortedSet

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        store = SortedSet()
        index = -(x - 1)
        mini = float('inf')

        for num in nums:
            if store:
                idx = bisect_left(store, num)
                
                if idx >= len(store):
                    mini = min(mini, abs(num - store[-1]))
                else:
                    mini = min(mini, abs(num - store[idx]))
                if idx < len(store) - 1:
                    mini = min(mini, abs(num - store[idx + 1]))
                if idx > 0:
                    mini = min(mini, abs(num - store[idx - 1]))

            if index >= 0 and index < len(nums):
                store.add(nums[index])

            index += 1
        
        return mini if mini != float('inf') else 0

        