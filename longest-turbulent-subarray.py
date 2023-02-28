class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = False
        down = False
        start = 0
        length = len(arr)
        maxi = 1        

        for end in range(1, length):
            if arr[end-1] < arr[end]:
                if up == True and down == False:
                    start = end - 1
                    print(start)
                up = True 
                down = False
            elif arr[end-1] > arr[end]:
                if up == False and down == True:
                    start = end - 1
                    print(start)
                up = False 
                down = True
            else:
                up = False
                down = False                
                start = end
                print(start)
            maxi = max(maxi, end - start + 1)

        return maxi