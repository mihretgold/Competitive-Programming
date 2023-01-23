class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxi = max(arr)
        m = arr.index(maxi)
        length = len(arr)
        check = True
        countleft = 0
        countright = 0
        if length < 3:
            return False
        for index in range(m):
            if arr[index] >= arr[index+1]:
                check = False
                break
            else:
                countleft += 1
                
        for index in range(m, length-1):
            if arr[index] <= arr[index+1]:
                check = False
                break
            else:
                countright += 1
                
        if countleft == 0 or countright == 0:
            check = False
                
        return check
                