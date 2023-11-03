class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        idx = 0
        length = len(target)
        answer = []
        
        for index in range(1, n + 1):
            if idx >= length:
                break
                
            answer.append("Push")
            
            if index == target[idx]:
                idx += 1
            else:
                answer.append("Pop")
                
        return answer