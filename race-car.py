class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        answer = 0
        count = 0
        visted = set()
        visted.add((0, 1))

        while queue:
            length = len(queue)
            for _ in range(length):

                position, speed = queue.popleft()
                
                if position == target:
                    answer = count 
                    return count

                A = position + speed
                A_speed = speed * 2
                if (A, A_speed) not in visted:
                    queue.append((A, A_speed))
                    visted.add((A, A_speed))
                    

                R_speed = -1
                if speed <= 0:
                    R_speed = 1

                if (position, R_speed) not in visted:
                    queue.append((position, R_speed))
                    visted.add((position, R_speed))
            count += 1
        # return answer