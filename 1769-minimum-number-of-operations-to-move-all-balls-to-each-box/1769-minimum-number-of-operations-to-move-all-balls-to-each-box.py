class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        length = len(boxes)
        for row in range(length):
            count = 0 
            for col in range(length):
                if boxes[col] == '1':
                    count += abs(col-row)
            answer.append(count)
            
        return answer