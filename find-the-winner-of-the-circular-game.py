class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        count = 0
        losser = 0
        index = 0
        while index < n and losser < n-1:
            if arr[index] != -1:
                count += 1
            if count == k:
                arr[index] = -1
                count = 0
                losser += 1
            
            if index == n-1:
                index = 0
            else:
                index += 1
        ans = 0
        for num in arr:
            if num != -1:
                ans = num
                break

        return ans