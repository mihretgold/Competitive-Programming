class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        visted = set("0000")
        deadends = set(deadends)

        if "0000" in deadends:
            return -1
        
        answer = -1
        count = 0
        found = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                wheel = queue.popleft();
                if wheel == target:
                    answer = count
                    found = 1
                    break

                foundAdd = 0
                foundSub = 0
                for i in range(4):
                    num = int(wheel[i])
                    add = 0
                    sub = 9
                    if num != 9:
                        add = num + 1
                    
                    if num != 0:
                        sub = num - 1

                    wheelAdd = wheel[:i] + str(add) + wheel[i+1:]
                    wheelSub =  wheel[:i] + str(sub) + wheel[i+1:]

                    if wheelAdd in deadends or wheelAdd in visted:
                        foundAdd = 1

                    if wheelSub in deadends or wheelSub in visted:
                        foundSub = 1
                    
                    if foundAdd == 0:
                        queue.append(wheelAdd)
                        visted.add(wheelAdd)
                    if foundSub == 0:
                        queue.append(wheelSub)
                        visted.add(wheelSub)
                    foundAdd = 0
                    foundSub = 0
            count += 1
            if found == 1:
                break
        

        return answer