class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        map_check = {}
        length = len(arr)
        for index in range(length):
            map_check[arr[index]] = index
        
        for index in range(length):
            double= 2 * arr[index]
            if double in map_check and index != map_check[double]:
                return True
            
        return False
        
        
        