class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        length = len(arr)
        for i in range(length-1, -1, -1):
            if(arr[i] != i+1):
                
                k =0
                while arr[k] != i+1: 
                    k += 1
                ans.append(k+1)
                arr[:k+1] = arr[:k+1][::-1]
                arr[:i+1] = arr[:i+1][::-1]
                ans.append(i+1)
                
        return ans
            