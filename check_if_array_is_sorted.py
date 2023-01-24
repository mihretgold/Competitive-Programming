class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        count = 0
        for i in range(n-1):
            if arr[i] <= arr[i+1]:
                count += 1
            else: 
                break
        if count == n-1:
            return 1
        else:
            return 0
