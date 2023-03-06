class Solution:       
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        while low <= high:
            mid = low + (high - low)//2
            sums = 0
            for num in piles:
                sums += ceil(num/mid)
            if sums <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low