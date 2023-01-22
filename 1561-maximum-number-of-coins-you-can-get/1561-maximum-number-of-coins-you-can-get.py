class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        length = len(piles)
        sum = 0
        piles.sort()
        for index in range(length-2, (length//3)-1, -2):
            sum += piles[index]
            
        return sum