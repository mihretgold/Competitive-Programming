class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins = 0
        length = len(arr)
        
        for index in range(1, 2 * length):
            idx = index % length
            if idx == 0:
                continue
                
            if arr[0] >= arr[idx]:
                wins += 1
            else:
                arr[0], arr[idx] = arr[idx], arr[0]
                wins = 1
                
            if wins >= k:
                return arr[0]
            
        return arr[0]
                
        