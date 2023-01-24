class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        large = -1
        for index in range(length -1, -1, -1):
            if arr[index] > large:
                arr[index], large = large ,arr[index]
            else:
                arr[index] = large       
            
        return arr