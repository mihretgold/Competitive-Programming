class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        arr = []
        answer = [0] * length
        
        for index in range(length):
            arr.append((ratings[index], index))
            
        arr.sort()
        
        for val, index in arr:
            left = 0
            right = 0
            
            if index - 1 >= 0 and ratings[index - 1] != val:
                left = answer[index - 1]
            
            if index + 1 < length and ratings[index + 1] != val:
                right = answer[index + 1]
                
            answer[index] = max(left, right) + 1
        
        result = sum(answer)
        
        return result
                
                