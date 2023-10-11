class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        answer = [0] * len(people)
        flowers.sort()
        lowerBound, upperBound = zip(*flowers)
        upperBound = sorted(upperBound)

        
        def binaryRight(search):
            low = 0
            high = len(flowers) - 1
            
            while low <= high:
                mid = low + (high - low)//2
                
                if flowers[mid][0] <= search:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return high
        
        def binaryLeft(search):
            low = 0
            high = len(upperBound) - 1
            
            while low <= high:
                mid = low + (high - low)//2
                
                if upperBound[mid] >= search:
                    high = mid - 1   
                else:
                    low = mid + 1
                   
                    
            return low
                
                
        
        for index, person in enumerate(people):
            lower = binaryRight(person)
            upper = binaryLeft(person)
            answer[index] = (lower - upper + 1)
            
        return answer