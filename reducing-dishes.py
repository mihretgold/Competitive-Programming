class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int: 
        satisfaction.sort()
        length = len(satisfaction)
        sums = 0
        total = 0
      
        for index in range(length-1, -1, -1):
            total += satisfaction[index]
            
            new_sum = sums + total
            if sums > new_sum:
                return sums
            else:
                sums = new_sum

        return sums