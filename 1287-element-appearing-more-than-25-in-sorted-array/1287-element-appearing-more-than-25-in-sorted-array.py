class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        count = Counter(arr)
        target = length // 4 
        
        for num in count:
            if count[num] > target:
                return num
            
        return -1