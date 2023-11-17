class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        length = len(meetings)
        heap = []
        maxx = 0 
        i = 0
        meetings.sort()

        for index in range(length):
            start, end = meetings[index]
            diff = end - start
            if (not heap or heap[0][0] > start) and i < n:
                heappush(heap, (0, i, 0))
                i += 1
            store = []
            found = (0, n, 0)
            if heap and heap[0][0] <= start: 
                while heap and heap[0][0] <= start:  
                    total, idx, count = heappop(heap)     
                    if  found[1] > idx:
                        found = (total, idx, count)
                    store.append((total, idx, count))
                # print(store, heap)
                for a, b, c in store:
                    if (a, b, c) != found:
                        heappush(heap, (a, b, c))
            else:
                found = heappop(heap)

            # print(heap)
            maxx = max(maxx, found[2] + 1)      
            heappush(heap, (max(end, found[0] + diff), found[1], found[2] + 1))
        # print(maxx)
        # print(heap)

        mini = n
        for _, idx, count in heap:
            if count == maxx:
                mini = min(mini, idx)

        return mini
            