class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        lengthHeaters = len(heaters)
        lengthHouse = len(houses)
        maxi = 0
        hIndex = 0

        heaters.sort()
        houses.sort()

        for index in range(lengthHouse):
            value = 0
            val = 0
            val2 = -1
            while val >= val2 and hIndex < lengthHeaters -1:
                val = abs(houses[index] - heaters[hIndex])
                val2 = abs(houses[index] - heaters[hIndex + 1])
                if val >= val2:
                    hIndex += 1           
                

            maxi = max(maxi, abs(heaters[hIndex] - houses[index]))
            
        return maxi