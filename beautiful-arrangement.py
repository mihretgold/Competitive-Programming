class Solution:
    def countArrangement(self, n: int) -> int:
        unique = 0
        beauty = 0

        def calcArrange(index, path):
            nonlocal beauty
            nonlocal unique
            if path and ((path[-1] % len(path) != 0) and (len(path) % path[-1] != 0)):
                return
            if len(path) == n:
                beauty += 1
                return             

            for i in range(1, n+1):
                if unique & 1 << i == 0:
                    path.append(i)
                    unique |= 1 << i
                    calcArrange(i+1, path[:])
                    path.pop()
                    unique ^= 1 << i

        calcArrange(1, [])
        
        return beauty