class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        length = len(arr)
        maxi = (float('-inf'), -1)
        index = length-1
        while index > 0:
            if arr[index-1] > arr[index]:
                break
            index -= 1
        
        if index <= 0:
            return arr

        j = length-1
        while j > index-1:
            if arr[j] >= maxi[0] and arr[j] < arr[index-1]:
                maxi = (arr[j], j)
            j -= 1

        arr[index-1], arr[maxi[1]] = arr[maxi[1]], arr[index-1]


        return arr