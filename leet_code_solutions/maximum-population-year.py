class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        mini = min(logs, key = lambda x: x[0])[0]
        maxx = max(logs, key = lambda x: x[1])[1]
        length = maxx - mini + 1
        answer = [0] * length
        maxxIndex = 0

        for birth, death in logs:
            answer[birth - mini] += 1
            answer[death - mini] -= 1

        for index in range(1, length):
            answer[index] += answer[index - 1]
            if answer[index] > answer[maxxIndex]:
                maxxIndex = index

        maxxIndex += mini
        return maxxIndex

        
        
        