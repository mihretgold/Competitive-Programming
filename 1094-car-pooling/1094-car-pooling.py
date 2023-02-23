class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0 for _ in range(1002)]
        for num, start, end in trips:
            prefix[start] += num
            prefix[end] -= num
            
        for index in range(1, 1002):
            prefix[index] += prefix[index-1]
            
        for index in range(1002):
            if prefix[index] > capacity:
                return False
            
        return True