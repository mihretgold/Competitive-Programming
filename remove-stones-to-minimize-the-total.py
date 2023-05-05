class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapify(piles)
        index = 0
        size = len(piles)

        while index < k and piles:
            greatest = heappop(piles)
            greatest = floor(greatest/2)
            heappush(piles, greatest)
            index += 1
       
        return -sum(piles)