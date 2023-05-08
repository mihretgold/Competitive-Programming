class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        length = len(tasks)
        heap = []
        answer = []

        for index in range(length):
            tasks[index].append(index)
        
        tasks.sort()
        time = tasks[0][0]
        index = 0
        while index < length:
            while index < length and tasks[index][0] <= time:
                heappush(heap, (tasks[index][1], tasks[index][2]))
                index += 1

            process_time, idx = heappop(heap)
            time += process_time
            answer.append(idx)
            if not heap and index < length and time < tasks[index][0] :
                time = tasks[index][0]
        while heap:
            process_time, idx = heappop(heap)
            answer.append(idx)
        
        return answer