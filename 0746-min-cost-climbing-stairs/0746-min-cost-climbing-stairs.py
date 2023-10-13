class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        left = cost[0]
        right = cost[1]
        

        for index in range(2, n ):
            val =  min(left, right) + cost[index]
            left = right
            right = val 

        return min(left, right)
