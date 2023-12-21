class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []
        length = len(points)
        
        for x, y in points:
            arr.append(x)
            
        arr.sort()
        answer = 0
        for idx in range(1, length):
            answer = max(answer, arr[idx] - arr[idx - 1])
            
            
        return answer
        