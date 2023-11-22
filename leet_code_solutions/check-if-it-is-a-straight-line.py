class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length = len(coordinates) 
        if (coordinates[1][0] ==  coordinates[0][0]):
            val = coordinates[1][0] 
            for index in range(length):
                if coordinates[index][0] !=  val:
                    return False
                    break
            else:
                return True
        slope =( coordinates[1][1] -  coordinates[0][1])/( coordinates[1][0] -  coordinates[0][0])
        check = True

        for index in range(1, length):
            if coordinates[index][0] == coordinates[index - 1][0]:
                check = False 
                break
            temp= (coordinates[index][1] -  coordinates[index-1][1])/( coordinates[index][0] - coordinates[index - 1][0])
            if temp != slope:
                check = False
                break

        return check
