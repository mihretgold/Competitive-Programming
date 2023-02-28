class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        length = len(tickets)
        count = 0

        while queue[k] > 0:
            if queue[0] > 0:
                queue[0] -= 1 
                count += 1
            temp = queue.popleft()
            queue.append(temp)
                
            k -= 1
            k %= length
        
        return count