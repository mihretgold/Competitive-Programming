class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        fleet = []
        stack = []
        for index in range(length):
            pos = target - position[index]
            t = pos / speed[index]
            fleet.append((pos, t))
            
        fleet.sort()
        for index in range(length):
            if len(stack) != 0 and stack[-1] < fleet[index][1]:
                stack.append(fleet[index][1])
            elif len(stack) == 0:
                stack.append(fleet[index][1])
                
        return len(stack)