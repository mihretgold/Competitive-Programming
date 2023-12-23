class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visted = set()
        direction = {"N":(0, 1), "E":(1, 0), "W":(-1, 0), "S": (0, -1)}
        start = (0, 0)
        visted.add(start)
        
        for s in path:
            start = (start[0] + direction[s][0], start[1] + direction[s][1])
            if start in visted:
                return True
            visted.add(start)
            
        return False
        