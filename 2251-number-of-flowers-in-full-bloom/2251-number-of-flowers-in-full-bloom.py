class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        length = len(people)
        answer = [0] * length
        
        flowers.sort()
        
        lowerBound, upperBound = zip(*flowers)
        # lowerBound = list(lowerBound)
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
        
        def binaryLeft(arr, search):
            low = 0
            high = len(arr) - 1
            # print(arr, search)
            
            while low <= high:
                mid = low + (high - low)//2
                
                if arr[mid] >= search:
                    high = mid - 1   
                else:
                    low = mid + 1
                   
                    
            return low
                
                
        
        for index in range(length):
            bloomed = binaryRight(people[index])
            upper = binaryLeft(upperBound, people[index])
            # print(bloomed, upper)
            answer[index] = (bloomed - upper + 1)
            
        return answer