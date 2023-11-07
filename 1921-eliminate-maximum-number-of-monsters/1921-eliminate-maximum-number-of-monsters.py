class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = 0
        timeArr = []
        length = len(dist)
        answer = 0
        
        for index in range(length):
            timeArr.append(dist[index]/speed[index])
            
        timeArr.sort()
        
        for index in range(length):
            diff = timeArr[index] - time
            if diff > 0:
                time += 1
            else:
                break
                
        return time
                
        
        