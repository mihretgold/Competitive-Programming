class Solution:
    def maxFrequencyScore(self, A: List[int], k: int) -> int:
        prefix = list(accumulate(sorted(A), initial = 0))
        low = 1
        high = len(A) 
        length = len(A)
        answer = 0
        A.sort()
        
        while low <= high:
            mid = low + (high - low)//2
            start = 0
            for end in range(length):
                if end - start + 1 > mid:
                    start += 1
                if end - start + 1 == mid:
                    target = (end - start) // 2 + start
                    targetValue = A[target]
                    left = (targetValue * (target - start + 1)) - (prefix[target + 1] - prefix[start])
                    right = (prefix[end+1] - prefix[target + 1]) - (targetValue * (end - target))
                    if left + right <= k:
                        # print("in")
                        low = mid + 1
                        answer = mid
                        break
                
            else:
                high = mid - 1
                
        return answer
                    
                    
                
        