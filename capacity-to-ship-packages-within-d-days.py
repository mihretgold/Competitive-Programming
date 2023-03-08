class Solution:
    # check when count is actually 1
    def checkCapacity(self, weights, days, k):
        sums = 0
        count = 1
        for weight in weights:
            sums += weight
            if sums > k:
                count += 1
                sums = weight

        return count <= days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = low + (high - low)//2
            if self.checkCapacity(weights, days, mid):
                high = mid - 1
            else:
                low = mid + 1


        return low